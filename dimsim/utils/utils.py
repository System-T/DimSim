import sys
import math
from pypinyin import pinyin, lazy_pinyin, Style

from dimsim.utils.maps import consonantMap_TwoDCode, vowelMap_TwoDCode, hardcodeMap

def to_pinyin(utterance):
    length = len(utterance)
    translated = []
    pinyin_encodings = pinyin(utterance, style=Style.TONE2)
    for i in range(length):
        currPinyin = pinyin_encodings[i][0]
        translated.append(put_tone_to_end(currPinyin))
    return translated

def put_tone_to_end(input_pinyin):
    if len(input_pinyin) is 1:
        return input_pinyin + '1'
    tone_index = 0
    tone = '1'
    for index, character in enumerate(input_pinyin):
        if character in ("1","2","3","4"):
            tone_index = index
            tone = input_pinyin[index]
            break
    if tone_index is 0:
        return input_pinyin + "5"
    return input_pinyin[0:index] + input_pinyin[index+1:] + tone

def get_edit_distance_close_2d_code(a, b):
    res = 0
    try:
        if (a is None) or (b is None):
            print("Error:pinyin({},{})".format(a.toString(),b.toString()))
            return res
        
        twoDcode_consonant_a = consonantMap_TwoDCode[a.consonant]
        twoDcode_consonant_b = consonantMap_TwoDCode[b.consonant]
        
        cDis = abs(get_distance_2d_code(twoDcode_consonant_a, twoDcode_consonant_b))
        
        twoDcode_vowel_a = vowelMap_TwoDCode[a.vowel]
        twoDcode_vowel_b = vowelMap_TwoDCode[b.vowel]
        
        vDis = abs(get_distance_2d_code(twoDcode_vowel_a, twoDcode_vowel_b))

        hcDis = get_sim_dis_from_hardcod_map(a,b)
        
        res = min((cDis+vDis),hcDis) + 1.0*abs(a.tone-b.tone)/10
        
    except:
        raise Exception("Error pinyin {}{}".format(a.toString(), b.toString()))
    return res

def get_sim_dis_from_hardcod_map(a, b):
    try:
        simPy = hardcodeMap[a.toStringNoTone()]
        if simPy is not None:
            if simPy is b.toStringNoTone():
                return 2.0
        else:
            simPy=hardcodeMap[b.toStringNoTone()]
            if simPy is not None and simPy is a.toStringNoTone():
                return 2.0
        return sys.float_info.max
    except:
        return sys.float_info.max

def get_distance_2d_code(X, Y):
    x1, x2 = X
    y1, y2 = Y

    x1d = abs(x1-y1)
    x2d = abs(x2-y2)
    
    return math.sqrt( x1d**2 + x2d**2)