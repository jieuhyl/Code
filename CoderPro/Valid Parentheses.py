# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:02:45 2020

@author: Jie.Hu
"""


# Valid Parentheses

class solution(object):
    def validpar(self, s):
        
        if len(s)%2 != 0:
            return False
        
        mapping = {'}':'{', ']':'[', ')':'('}
        
        res = [None]
        for p in s:
            if p in mapping and mapping[p] == res[-1]:
                res.pop()
            else:
                res.append(p)
        return res == [None]

s = '{[()]}()'
s = '()[]{}'
print(solution().validpar(s))
