# DimSim - A Chinese Soundex Library (Python version) 

DimSim is developed by a research team at IBM Almaden Research Center. 

pypi project: https://pypi.org/project/chinesesoundex/

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following paper:

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018. [link to paper](https://underconstruction)

In this library, we provide a pre-trained model that can:
- given two Chinese phrases (of the same length), return the phonetic distance of the input phrases.
- given a Chinese phrase, return its top-k similar (phoentically) Chinese phrases.



## How to install

**Dependencies**:
- [pypinyin](https://github.com/mozillazg/python-pinyin): used for translating Chinese characters into their correponding pinyins. 

There are two ways to install this library:
- Download the source code from the **code** folder and compile it yourself.
- run the following script to install
```shell
pip install chinesesoundex
```

## How to use

Computing phonetic distance of two Chinese phrases
```python
dist = get_distance("大侠","大虾")
0.0002380952380952381

dist = get_distance("大侠","大人")
25.001417183349876
```
***
Return top-k phonetically similar phrases of a given Chinese phrase. Two parameters:
- **model** controls the character type of the returned Chinese phrases, where 'simplified' represents simplified Chinese and 'traditional' represents traditional Chinese.
- **theta** controls the size of search space for the candidate phrases.
```python
candidates = getCandidates("大侠", model="simplified", theta=1)
['打下', '大虾', '大侠']

candidates = getCandidates("粉丝", mode="traditinoal", theta=1)
['門市', '分時', '焚屍', '粉飾', '粉絲']
```

