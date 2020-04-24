# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:42:22 2020

@author: Jie.Hu
"""


# Group Words that are Anagrams
import collections

class solution(object):
    def group1(self, strs):
        dct = {}
        for s in strs:
            if ''.join(sorted(s)) in dct:
                dct[''.join(sorted(s))].append(s)
            else:
                dct[''.join(sorted(s))] = [s]
        return tuple(dct.values())
    
    def group2(self, strs):
        dct = collections.defaultdict(list)
        for s in strs:
            dct[''.join(sorted(s))].append(s)
        return tuple(dct.values())
    
    def hashkey1(self, s):
        return ''.join(sorted(s))
    
    def hashkey2(self, s):
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] = 1
        return tuple(arr)
    
    def group3(self, strs):
        dct = collections.defaultdict(list)
        for s in strs:
            dct[self.hashkey2(s)].append(s)
        return tuple(dct.values())
    
strs = ['abc', 'bcd', 'cba', 'cbd', 'efg']  
print(solution().group3(strs))
        

