# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:34:27 2020

@author: Jie.Hu
"""


# First Recurring Character

class solution(object):
    def firstcur(self,s):
        res = set()
        for i in s:
            if i in res:
                return i
            res.add(i)
        return []
    
    def firstcur2(self, s):
        res = dict()
        for i in s:
            if i in res:
                return i
            res[i] = 1
        return []
s = 'qertwet'
print(solution().firstcur2(s))