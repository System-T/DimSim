import os
import pickle

from pypinyin import pinyin, lazy_pinyin, Style
from dimsim.utils import maps

class Pinyin:
    consonantList = maps.consonantList
    vowelList = maps.vowelList
    
    def __init__(self, pinyinstr):
        self.tone = int(pinyinstr[-1])
        self.locp = pinyinstr[0:-1].lower()
        self.consonant, self.vowel = self.parseConsonant(self.locp)
        self.pinyinRewrite()
    
    def parseConsonant(self, pinyin):
        for consonant in self.consonantList:
            if pinyin.startswith(consonant):
                return (consonant, pinyin[len(consonant):])
        # it's a vowel without consonant
        if pinyin in self.vowelList:
            return None, pinyin.lower()
        
        print("Invalid Pinyin, please check!")
        return None, None
        
    def toStringNoTone(self):
        return "{}{}".format(self.consonant, self.vowel)
    
    def toStringWithTone(self):
        return "{}{}{}".format(self.consonant, self.vowel, self.tone)
    
    def toString(self):
        return "{}{}{}".format(self.consonant, self.vowel, self.tone)
        
    def pinyinRewrite(self):
        import re
        yVowels = {"u","ue","uan","un","u:","u:e","u:an","u:n"}
        tconsonant = {"j","g","x"}
        if 'v' in self.vowel:
            self.vowel = self.vowel.replace("v", "u:")
            
        if self.consonant is None or self.consonant is "":
            self.consonant = ""
            return
        if self.consonant is "y":
            if self.vowel in yVowels:
                if "u:" not in self.vowel:
                    self.vowel = self.vowel.replace("u","u:")
            else:
                self.vowel="i"+self.vowel
                regex = re.compile("i+")
                self.vowel = self.vowel.replace("iii","i")
                self.vowel = self.vowel.replace("ii","i")
            self.consonant=""
        
        if self.consonant is "w":
            self.vowel="u"+self.vowel
            self.vowel=self.vowel.replace("uuu","u")
            self.vowel=self.vowel.replace("uu","u")
            self.consonant = ""
        
        if (self.consonant in tconsonant) and (self.vowel is "u") or (self.vowel is "v"):
            self.vowel="u:"
        
        if self.vowel is "iou":
            self.vowel = "iu"
        
        if self.vowel is "uei":
            self.vowel = "ui"
        
        if self.vowel is "uen":
            self.vowel = "un"

def load_pinying_to_simplified():

    curr_dir, _ = os.path.split(__file__)
    root_dir, _ = os.path.split(curr_dir)
    DATA_PATH = os.path.join(root_dir, "data", "pinyin_to_simplified.pickle")
    sfile = open(DATA_PATH, 'rb')
    pinyin_to_simplified = pickle.load(sfile)
    sfile.close()
    return pinyin_to_simplified


def load_pinying_to_traditional():

    curr_dir, _ = os.path.split(__file__)
    root_dir, _ = os.path.split(curr_dir)
    DATA_PATH = os.path.join(root_dir, "data", "pinyin_to_traditional.pickle")
    tfile = open(DATA_PATH, 'rb')
    pinyin_to_traditional = pickle.load(tfile)
    tfile.close()
    return pinyin_to_traditional
    