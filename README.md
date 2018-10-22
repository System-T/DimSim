# DimSim - A Chinese Soundex Library in Python

## Overview
We provide a phonetic algorithm for indexing Chinese characters by sound. The technical details can be found in the following paper:

Min Li, Marina Danilevsky, Sara Noeman and Yunyao Li. *DIMSIM: An Accurate Chinese Phonetic Similarity Algorithm based on Learned High Dimensional Encoding*. CoNLL 2018. [link to paper](https://underconstruction)

In this library, we provide a pre-trained model that can:
- given two Chinese phrases (of the same length), return the phonetic distance of the input phrases.
- given a Chinese phrase, return its top-k similar (phoentically) Chinese phrases.
