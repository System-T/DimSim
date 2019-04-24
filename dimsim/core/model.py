from pypinyin import pinyin, lazy_pinyin, Style
import sys
import math
import itertools
import os

from dimsim.utils.pinyin import Pinyin, load_pinying_to_simplified, load_pinying_to_traditional
from dimsim.utils.utils import get_edit_distance_close_2d_code, to_pinyin
from dimsim.utils.maps import vowelMap, consonantMap

doubleConsonantsMap = {}
doubleVowelsMap = {}

pinyin_to_simplified = load_pinying_to_simplified()
pinyin_to_traditional = load_pinying_to_traditional()

def get_distance(utterance1, utterance2, pinyin=False):
    '''
    Calculates the distances between embeddings of two Chinese words.
    input: 
        utterance1, utterance2: utf-8 strings for Chinese words or 
                                pinyin strings.
        pinyin : Boolean - indicates if words are in Chinese or Pinyin.
    output:
        distance - float.
    '''
    assert (len(utterance1) == len(utterance2)),"The two inputs do not have the same length"

    if not pinyin:
        u1 = to_pinyin(utterance1)
        u2 = to_pinyin(utterance2)
    
    else:
        u1 = utterance1
        u2 = utterance2
    
    la = []
    lb = []
    for py in u1:
        la.append(Pinyin(py))
    for py in u2:
        lb.append(Pinyin(py))


    res = 0.0
    numDiff = 0        
    tot = len(utterance1)*2.1
    for i in range (len(utterance1)):
        apy = la[i]
        bpy = lb[i]

        if (apy is None) or (bpy is None):
            raise Exception("!Empty Pinyin {},{}".format(la, lb))
        res += get_edit_distance_close_2d_code(apy, bpy)
        
        if apy.consonant is not bpy.consonant:
            numDiff+=1
        
        if not(str(apy.vowel) == str(bpy.vowel)):
            numDiff+=1
        
        if apy.tone is not bpy.tone:
            numDiff+=0.01
            
    diffRatio = (numDiff)/tot
    return res*diffRatio      
        

def get_candidates(sentence, mode="simplified", theta=1):
    '''
    Gets similar sounding words / candidates based on embeddings.
    inputs:
        sentence - utf-8 string with the Chinese words.
    outputs:
        candidates - a list containing utf-8 string Chinese words.
    '''    
    candidates = []
    words_candidates = []
    for word in sentence:
        candid = _get_close_pinyin_candids(word, theta)
        words_candidates.append(candid)
    all_combinations = itertools.product(*words_candidates)
    counter = 0
    for combination in all_combinations:
        counter+=1
        searchKey = ""
        for i in combination:
            searchKey = searchKey + i.toStringWithTone().replace("None","") + " "
        if mode is "simplified":
            if searchKey.strip() in pinyin_to_simplified:
                candidates+=pinyin_to_simplified[searchKey.strip()]
        else:
            if searchKey.strip() in pinyin_to_traditional:
                candidates+=pinyin_to_traditional[searchKey.strip()]
    return candidates


def _get_close_pinyin_candids(word, theta=2):
    res = []
    word_pinyin = to_pinyin(word)
    word_py = Pinyin(word_pinyin[0])
    
    cCandids = _get_consonant_candids(theta, word_py)
    for i in range(len(cCandids)):
        if cCandids[i] == word_py.consonant:
            continue
        for j in range(1,5,1):
            newPy = cCandids[i]+word_py.vowel+str(j)
            res.append(Pinyin(newPy))
    
    vCandids = _get_vowel_candids(theta, word_py)
    for i in range(len(vCandids)):
        for j in range(1,5,1):
            if word_py.consonant is None:
                newPy = vCandids[i]+str(j)
            else:
                newPy = word_py.consonant+vCandids[i]+str(j)
            res.append(Pinyin(newPy))
    return res
    
def _get_consonant_candids(theta, word_py):
    _populate_double_consonants_map()
    res = []
    if word_py.consonant is None:
        orgCode = consonantMap["__v"]
    else:
        orgCode = consonantMap[word_py.consonant]
        for i in range(int(orgCode-theta), int(orgCode+theta), 1):
            if float(i) in doubleConsonantsMap:
                cand = doubleConsonantsMap[float(i)]
                if cand is not None:
                    res += cand
    return res
    

def _get_vowel_candids(theta, word_py):
    _populate_double_vowels_map()
    res = []       
    orgCode = vowelMap[word_py.vowel]
    for i in range(int(orgCode-theta), int(orgCode+theta), 1):
        if float(i) in doubleVowelsMap:
            cand = doubleVowelsMap[float(i)]
            if cand is not None:
                res += cand
    return res

def _populate_double_consonants_map():
    if len(doubleConsonantsMap) is not 0:
        return
    hmCdouble = consonantMap
    for consonant in hmCdouble:
        if hmCdouble[consonant] not in doubleConsonantsMap:
            doubleConsonantsMap[hmCdouble[consonant]] = []
            
        doubleConsonantsMap[hmCdouble[consonant]].append(consonant)
        
def _populate_double_vowels_map():
    if len(doubleVowelsMap) is not 0:
        return
    hmVdouble = vowelMap
    for vowel in hmVdouble:
        if hmVdouble[vowel] not in doubleVowelsMap:
            doubleVowelsMap[hmVdouble[vowel]] = []
            
        doubleVowelsMap[hmVdouble[vowel]].append(vowel)  
