# DimSim - A Chinese Soundex Library (Python version) 

DimSim is developed by the Scalable Knowledge Intelligence team at IBM Almaden Research Center as part of the [SystemT](https://researcher.watson.ibm.com/researcher/view_group.php?id=1264) project. 

pypi project: https://pypi.org/project/chinesesoundex-1.0/

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following paper:

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018. [(link)](http://aclweb.org/anthology/K18-1043)

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
pip install chinesesoundex-1.0
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
candidates = getCandidates("大侠", mode="simplified", theta=1)
['打下', '大虾', '大侠']

candidates = getCandidates("粉丝", mode="traditinoal", theta=1)
['門市', '分時', '焚屍', '粉飾', '粉絲']
```

## Citation

Please cite the library by referencing the published paper:
```
@InProceedings{K18-1043,
  author = 	{Li, Min and Danilevsky, Marina and Noeman, Sara and Li, Yunyao},
  title = 	{{DIMSIM:} An Accurate Chinese Phonetic Similarity Algorithm Based on Learned High Dimensional Encoding},
  booktitle = 	{Proceedings of the 22nd Conference on Computational Natural Language Learning},
  year = 	{2018},
  publisher = 	{Association for Computational Linguistics},
  pages = 	{444-453},
  location = 	{Brussels, Belgium},
  url = 	{http://aclweb.org/anthology/K18-1043}
}
```
