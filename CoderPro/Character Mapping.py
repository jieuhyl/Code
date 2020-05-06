# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:12:15 2020

@author: Jie.Hu
"""


# Character Mapping

class solution(object):
    def charmap1(self, s, t):
        if len(set(s)) == len(set(t)):
            return True
        else:
            return False
    
    def charmap2(self, s, t):
        if len(s) != len(t):
            return False
        
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = t[i]
            else:
                if dct[s[i]] != t[i]:
                    return False
        return True

s = 'abc'
t = 'efg'
print(solution().charmap2(s,t))