# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:22:32 2020

@author: Jie.Hu
"""


# ransom note

s1 = 'aabdc'
s2 = 'aaabbcc'

def ransomnote(s1, s2):
    if len(set(s2)) < len(set(s1)):
        return False
    
    dct = {}
    
    for i in s2:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    
    for j in s1:
        if j not in dct:
            return False
        else:
            dct[j] -= 1
            if dct[j] < 0:
                return False
    return True
ransomnote(s1, s2)


import collections
def ransomnote(s1, s2):

    dct = collections.defaultdict(int)
    
    for i in s2:
        dct[i] += 1
        
    for j in s1:
        dct[j] -= 1
        if dct[j] < 0:
            return False
    
    return True
ransomnote(s1, s2)