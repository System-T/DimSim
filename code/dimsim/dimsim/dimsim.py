
# coding: utf-8

# In[656]:


from pypinyin import pinyin, lazy_pinyin, Style
import sys
import math
import itertools
import pickle
import os


# In[657]:


work_dir = os.path.abspath(__file__)
indexOfLastSlash = work_dir.rfind("/")
work_dir = work_dir[0:indexOfLastSlash]+"/"


# In[658]:


sfile = open(work_dir+'pinyin_to_simplified.pickle', 'rb')

# dump information to that file
pinyin_to_simplified = pickle.load(sfile)
sfile.close()

tfile = open(work_dir+'pinyin_to_traditional.pickle', 'rb')
pinyin_to_traditional = pickle.load(tfile)
tfile.close()


# In[659]:


def to_pinyin(utterance):
    length = len(utterance)
    translated = []
    pinyin_encodings = pinyin(utterance, style=Style.TONE2)
    for i in range(length):
        currPinyin = pinyin_encodings[i][0]
#         print("{} translates to {}".format(currPinyin, putToneToEnd(currPinyin)))
        translated.append(putToneToEnd(currPinyin))
    return translated

def putToneToEnd(input_pinyin):
    if len(input_pinyin) is 1:
        return input_pinyin + '1'
    tone_index = 0
    tone = '1'
    for index, character in enumerate(input_pinyin):
        if character in ("1","2","3","4"):
            tone_index = index
            tone = input_pinyin[index]
            break;
    if tone_index is 0:
        return input_pinyin + "5"
    return input_pinyin[0:index] + input_pinyin[index+1:] + tone

def get_distance(utterance1, utterance2):
    if(len(utterance1) is not len(utterance2)):
        print("the two inputs do not have the same length")
        return sys.float_info.max
    else:
        u1 = to_pinyin(utterance1)
        u2 = to_pinyin(utterance2)
        
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
                print("!Error {},{}".format(la, lb))
            
            res += getEditDistanceClose_TwoDCode(apy, bpy)
            
            if apy.consonant is not bpy.consonant:
                numDiff+=1
            
            if not(str(apy.vowel) == str(bpy.vowel)):
                numDiff+=1
            
            if apy.tone is not bpy.tone:
                numDiff+=0.01;
                
        diffRatio = (numDiff)/tot;
        a = 0
        if diffRatio is 0:
            a=1
        return res*diffRatio;
            
def getEditDistanceClose_TwoDCode(a, b):
    res = 0
    try:
        if (a is None) or (b is None):
            print("Error:pinyin({},{})".format(a.toString(),b.toString()))
            return res
        
        twoDcode_consonant_a = consonantMap_TwoDCode[a.consonant]
        twoDcode_consonant_b = consonantMap_TwoDCode[b.consonant]
        
        cDis = abs(getDistance_TwoDCode(twoDcode_consonant_a, twoDcode_consonant_b))
        
        twoDcode_vowel_a = vowelMap_TwoDCode[a.vowel]
        twoDcode_vowel_b = vowelMap_TwoDCode[b.vowel]
        
        vDis = abs(getDistance_TwoDCode(twoDcode_vowel_a, twoDcode_vowel_b))

        hcDis = getSimDisFromHardcodMap(a,b)
        
        res = min((cDis+vDis),hcDis) + 1.0*abs(a.tone-b.tone)/10
        
    except:
        print("Error pinyin {}{}".format(a.toString(), b.toString()))
        raise
    return res

def getSimDisFromHardcodMap(a, b):
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
    
    
def getDistance_TwoDCode(X, Y):
    x1, x2 = X
    y1, y2 = Y

    x1d = abs(x1-y1)
    x2d = abs(x2-y2)
    
    return math.sqrt( x1d**2 + x2d**2)


consonantMap_TwoDCode ={
    "b":(1.0,0.5),
    "p":(1.0,1.5), 

    "g":(7.0,0.5), 
    "k":(7.0,1.5), 
    "h":(7.0,3.0), 
    "f":(7.0,4.0), 

    "d":(12.0,0.5), 
    "t":(12.0,1.5), 

    "n":(22.5,0.5), 
    "l":(22.5,1.5), 
    "r":( 22.5,2.5), 

    
    "zh":(30,1.7), 
    "z":(30,1.5), 
    "j":(30.0,0.5), 

    "ch":(31,1.7), 
    "c":(31,1.5), 
    "q":(31.0,0.5), 

    "sh":(33,3.7),
    "s":(33,3.5),
    "x":(33,2.5),

    
    "m":(50.0,3.5), 

    "y":(40.0,0.0), 
    "w":(40,5.0),
    
    "":(99999.0,99999.0)
}


# In[662]:


vowelMap_TwoDCode = {
    "a":(1.0,0.0),
    "an":(1.0,1.0),
    "ang":(1.0,1.5),

    
    "ia":(0.0,0.0),
    "ian":(0.0,1.0),
    "iang":(0.0,1.5),

    "ua":(2.0,0.0),
    "uan":(2.0,1.0),
    "uang":(2.0,1.5),
    "u:an":(2.0,1.0),

    
    "ao":(5.0,0.0),
    "iao":(5.0,1.5),

    "ai":(8.0,0.0),
    "uai":(8.0,1.5),

    

    "o":(20,0.0),
    "io":(20,2.5),
    "iou":(20,4),
    "iu":(20,4),
    "ou":(20,5.5),
    "uo":(20,6.0),

    "ong":(20,8.0),
    "iong":(20,9.5),

    
    "er":(41,1),
    "e":(41,0.0),

    "u:e":(40,5.0),
    "ve":(40,5.0),
    "ue":(40,5.0),
    "ie":(40,4.5),
    "ei":(40,4.0),
    "uei":(40,3.0),
    "ui":(40,3.0),

    "en":(42,0.5),
    "eng":(42,1.0),

    "uen":(43,0.5),
    "un":(43,0.5),
    "ueng":(43,1.0),

    
    "i":(60,1.0),
    "in":(60,2.5),
    "ing":(60,3.0),

    "u:":(61,1.0),
    "v":(61,1.0),
    "u:n":(61,2.5),
    "vn":(61,2.5),

    "u":(80,0.0),

    "":(99999.0,99999.0)
}


# In[663]:


consonantList = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k","h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s","y", "w"]


# In[664]:


vowelList = ["a", "o", "e", "i", "u", "v","u:","er", "ao","ai", "ou","ei", "ia", "iao", "iu", "iou","ie", "ui","uei","ua","uo","uai", "u:e","ve",  "an", "en", "in", "un","uen", "vn","u:n","ian","uan", "u:an","van", "ang", "eng", "ing", "ong","iang","iong","uang","ueng"]


# In[665]:


class Pinyin:
    consonantList = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "zh", "ch", "sh", "r", "z", "c", "s","y", "w"]
    vowelList = ["a", "o", "e", "i", "u", "v","u:","er", "ao","ai", "ou","ei", "ia", "iao", "iu", "iou","ie", "ui","uei","ua","uo","uai", "u:e","ve",  "an", "en", "in", "un","uen", "vn","u:n","ian","uan", "u:an","van", "ang", "eng", "ing", "ong","iang","iong","uang","ueng"]
    
    def __init__(self, pinyinstr):
        self.tone = int(pinyinstr[-1])
        self.locp = pinyinstr[0:-1].lower()
        self.consonant, self.vowel = self.parseConsonant(self.locp)
#         print("before rewriting consonant={}, vowel={}, locp={}, tone={}".format(self.consonant,
#                                                                                self.vowel,
#                                                                                self.locp,
#                                                                                self.tone))
        self.pinyinRewrite()
#         print("after rewriting consonant={}, vowel={}, locp={}, tone={}".format(self.consonant,
#                                                                                self.vowel,
#                                                                                self.locp,
#                                                                                self.tone))
    
    def parseConsonant(self, pinyin):
        for consonant in consonantList:
            if pinyin.startswith(consonant):
                return (consonant, pinyin[len(consonant):])
        # it's a vowel without consonant
        if pinyin in vowelList:
            return None, pinyin.lower()
        
        print("Invalid Pinyin, please check!")
        return None, None
        
    def toStringNoTone(self):
        return "{}{}".format(self.consonant, self.vowel)
    
    def toStringWithTone(self):
        return "{}{}{}".format(self.consonant, self.vowel, self.tone)
    
    def toString(self):
        print("{}{}{}".format(self.consonant, self.vowel, self.tone))
        
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
            self.vowel="u"+self.vowel;
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
        
                
        
        


# In[666]:


hardcodeMap = {
    "hua":"fa",
    "fa":"hua",
    "huan":"fan",
    "fan":"huan",
    "hui":"fei",
    "jie":"zhe",
    "kou":"ke",
    "gou":"ge",
    "zhong":"zen",
    "san":"shang"
}


# In[667]:


consonantMap = {
    "b":1.0,
    "p":2.0,
    
    "m":11.0,
    "f":12.0,
    
    "d":21.0,
    "t":22.0,
    
    "n":31.0,
    "l":31.0,
    "r":32.0,
    
    "g":41.0,
    "k":42.0,
    "h":43.0,
    
    "j":46.0,
    "q":47.0,
    "x":48.0,
    
    "z":61.0,
    "c":62.0,
    
    "zh":71.0,
    "ch":72.0,
    
    "sh":81.0,
    "s":82.0,
    
    "y":90.0,
    "w":100.0,
    
    "":99999.0,
    "__v":99999.0
}


# In[668]:


vowelMap = {
    "ia":0.0,
    "a":2.0,
    "ai":3.0,
    "uai":4.0,
    "iao":6.0,
    "ao":7.0,
    
    "uan":10.0,
    "an":11.0,
    "ang":12.0,
    "ian":14.0,
    "iang":15.0,
    "uang":17.0,
    "ua":18.0,
    
    "o":21.0,
    "io":22.0,
    "ou":23.0,
    "uo":24.0,
    "ong":26.0,
    "iong":27.0,
    
    "e":31.0,
    "ei":33.0,
    "ie":34.0,
    "er":37.0,
    
    "ve":40.0,
    "ue":40.0,
    "u:e":40.0,
    
    "en":43.0,
    "eng":44.0,
    
    "uen":45.0,
    "ueng":45.0,
    
    "u:en":42.0,
    "ven":42.0,
    
    "i":50.0,
    "u:":51.0,
    "v":51.0,
    "u:n":53.0,
    "vn":53.0,
    "u:an":55.0,
    "v:an":55.0,
    
    "in":53.0,
    "ing":55.0,
    
    "u":60.0,
    "ui":63.0,
    "uei":63.0,
    "iu":64.0,
    "iou":64.0,
    "un":66.0,
    
    "":99999.0,
    "__v":99999.0
}


# ### Get Pinyin Candidates that are close to an input pinyin

# In[644]:


doubleConsonantsMap = {}
doubleVowelsMap = {}

def getClosePinyinCandids(word, theta=2):
    res = []
    word_pinyin = to_pinyin(word)
    word_py = Pinyin(word_pinyin[0])
    
    cCandids = getConsonantCandids(theta, word_py)
    for i in range(len(cCandids)):
        if cCandids[i] == word_py.consonant:
            continue
        for j in range(1,5,1):
            newPy = cCandids[i]+word_py.vowel+str(j)
            res.append(Pinyin(newPy))
    
    vCandids = getVowelCandids(theta, word_py)
    for i in range(len(vCandids)):
        for j in range(1,5,1):
            if word_py.consonant is None:
#                 print(word_py.toStringWithTone(),"has none consonant")
                newPy = vCandids[i]+str(j)
            else:
                newPy = word_py.consonant+vCandids[i]+str(j)
            res.append(Pinyin(newPy))
    return res
            
    
    
def getConsonantCandids(theta, word_py):
    populateDoubleConsonantsMap()
    res = []
    curCode = 0        
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
    

def getVowelCandids(theta, word_py):
    populateDoubleVowelsMap()
    res = []
    curCode = 0        
    orgCode = vowelMap[word_py.vowel]
    for i in range(int(orgCode-theta), int(orgCode+theta), 1):
        if float(i) in doubleVowelsMap:
            cand = doubleVowelsMap[float(i)]
            if cand is not None:
                res += cand
    return res

def populateDoubleConsonantsMap():
    if len(doubleConsonantsMap) is not 0:
        return
    hmCdouble = consonantMap
    for consonant in hmCdouble:
        if hmCdouble[consonant] not in doubleConsonantsMap:
            doubleConsonantsMap[hmCdouble[consonant]] = []
            
        doubleConsonantsMap[hmCdouble[consonant]].append(consonant)
        
def populateDoubleVowelsMap():
    if len(doubleVowelsMap) is not 0:
        return
    hmVdouble = vowelMap
    for vowel in hmVdouble:
        if hmVdouble[vowel] not in doubleVowelsMap:
            doubleVowelsMap[hmVdouble[vowel]] = []
            
        doubleVowelsMap[hmVdouble[vowel]].append(vowel)        
        

def getCandidates(sentence, mode="simplified", theta=1):
    candidates = []
    words_candidates = []
    for word in sentence:
        candid = getClosePinyinCandids(word, theta)
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










