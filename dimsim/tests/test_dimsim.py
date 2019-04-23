# -*- coding: utf-8 -*-

# Standard libs
import io
import os
# Dependencies
import pytest

# The module to test
from dimsim.core.dimsim import get_distance, getCandidates

def test_distance_near():
        dist = get_distance('大侠','大虾')
        assert dist == 0.0002380952380952381

def test_distance_far():
        dist = get_distance('大侠','大人')
        assert dist == 25.001417183349876

def test_get_candidates_simplified():
        candidates = getCandidates('大侠', mode='simplified', theta=1)
        for c in candidates:
                assert c in ['打下', '大虾', '大侠']

def test_get_candidates_traditional():
        candidates = getCandidates('粉丝', mode='traditional', theta=1)
        for c in candidates:
                assert c in ['門市', '分時', '焚屍', '粉飾', '粉絲']

if __name__ == '__main__':
        pytest.main([__file__])
