# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:36:37 2020

@author: Jie.Hu
"""


# Valid Palindrome III

class solution(object):
    def valid(self, s):
        
        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        odd = 0
        for i, j in dct.items():
            if j%2 == 1:
                odd += 1
        return odd <= 1

s = "facebookfacebooktk"
print(solution().valid(s))