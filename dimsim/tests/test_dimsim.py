# -*- coding: utf-8 -*-

# Standard libs
import io
import os
# Dependencies
import pytest

# The module to test
from dimsim.core.dimsim import get_distance, get_candidates

def test_distance_near():
        dist = get_distance(u'大侠',u'大虾')
        assert dist == 0.0002380952380952381

def test_distance_far():
        dist = get_distance(u'大侠',u'大人')
        assert dist == 25.001417183349876

def test_distance_pinyin():
        dist = get_distance(['da4','xia2'],['da4','xia1'],pinyin=True)
        assert dist == 0.0002380952380952381

def test_invalid_input():
        pytest.raises(AssertionError, get_distance, u'大侠', u'大')

def test_get_candidates_simplified():
        candidates = get_candidates(u'大侠', mode='simplified', theta=1)
        for c in candidates:
                assert c in [u'打下', u'大虾', u'大侠']

def test_get_candidates_traditional():
        candidates = get_candidates(u'粉丝', mode='traditional', theta=1)
        for c in candidates:
                assert c in [u'門市', u'分時', u'焚屍', u'粉飾', u'粉絲']

if __name__ == '__main__':
        pytest.main([__file__])
