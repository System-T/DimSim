# DimSim - A Chinese Soundex Library (Python version) 

DimSim is a library developed by the Scalable Knowledge Intelligence team at IBM Almaden Research Center as part of the [SystemT](https://researcher.watson.ibm.com/researcher/view_group.php?id=1264) project. 

The PyPi project page can be found [here](https://pypi.org/project/dimsim/). It was created in collaboration with IBM Center for Open-Source Data and AI Technologies ([CODAIT](http://codait.org)).

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following [paper](http://aclweb.org/anthology/K18-1043):

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018.

In this library, we provide a pre-trained model that can perform the following functions, in compliance with the phonetic principles of Mandarin Chinese as guided by the Romanization defined in [ISO 7098:2015](https://www.iso.org/standard/61420.html):
- Given two Chinese phrases (of the same length), return the phonetic distance of the input phrases. Optionally you can feed in pinyin strings of Chinese phrases too.
- Given a Chinese phrase, return its top-k similar (phoentically) Chinese phrases.



## How to install

**Dependencies**:
- [pypinyin](https://github.com/mozillazg/python-pinyin): used for translating Chinese characters into their correponding pinyins. 

There are two ways to install this library:
- Install from PyPi

```shell
pip install dimsim
```
- Download the source code by cloning this repo and compile it yourself.

```shell
git clone git@github.com:System-T/DimSim.git

cd DimSim/

pip install -e .
```

## How to use
Once you have the package installed you can use it for the two functions as shown below.

- Computing phonetic distance of two Chinese phrases. The optional argument `pinyin` (False by default) can be used to provide a pinyin string list directly. See example usage below.

```python
import dimsim

dist = dimsim.get_distance("大侠","大虾")
0.0002380952380952381

dist = dimsim.get_distance("大侠","大人")
25.001417183349876

dist = dimsim.get_distance(['da4','xia2'],['da4','xia1']], pinyin=True)
0.0002380952380952381

dist = dimsim.get_distance(['da4','xia2'],['da4','ren2']], pinyin=True)
25.001417183349876

```
***
- Return top-k phonetically similar phrases of a given Chinese phrase. Two parameters:
- **mode** controls the character type of the returned Chinese phrases, where 'simplified' represents simplified Chinese and 'traditional' represents traditional Chinese.
- **theta** controls the size of search space for the candidate phrases.
```python
import dimsim

candidates = dimsim.get_candidates("大侠", mode="simplified", theta=1)
['打下', '大虾', '大侠']

candidates = dimsim.get_candidates("粉丝", mode="traditinoal", theta=1)
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
