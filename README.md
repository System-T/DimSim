# DimSim - A Chinese Soundex Library (Python version)

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following paper:

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018. [link to paper](https://underconstruction)

In this library, we provide a pre-trained model that can:
- given two Chinese phrases (of the same length), return the phonetic distance of the input phrases.
- given a Chinese phrase, return its top-k similar (phoentically) Chinese phrases.



## How to install

**Dependencies**: We use [pypinyin](https://github.com/mozillazg/python-pinyin) to convert Chinese characters into their correponding pinyins for internal computation. Install pypinyin before use our library

There are two ways to install this library:
- Download the source code from the **code** folder and compile it yourself.
- run `pip install dimsim` (pending, needs to upload to pypi)


## How to use

Computing phonetic distance of two Chinese phrases
```python
dist = get_distance("大侠","大虾")
0.0002380952380952381

dist = get_distance("大侠","大人")
25.001417183349876
```
***
Return top-k phonetically similar phrases of a given Chinese phrase
```python
candidates = getCandidates("大侠", model="simplified", theta=1)
['打下', '大虾', '大侠']

```python
candidates = getCandidates("粉丝", mode="traditinoal", theta=1)
['門市', '分時', '焚屍', '粉飾', '粉絲']
```

