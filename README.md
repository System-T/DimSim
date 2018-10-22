# DimSim - A Chinese Soundex Library (Python version)

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following paper:

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018. [link to paper](https://underconstruction)

In this library, we provide a pre-trained model that can:
- given two Chinese phrases (of the same length), return the phonetic distance of the input phrases.
- given a Chinese phrase, return its top-k similar (phoentically) Chinese phrases.



## How to install
There are two ways to install this library:
- Download the source code from the **code** folder and compile it yourself.
- run `pip install dimsim` (pending, needs to upload to pypi)

### Dependencies
We use [pypinyin](https://github.com/mozillazg/python-pinyin) to convert Chinese characters into their correponding pinyins for internal computation. Install pypinyin before use our library


