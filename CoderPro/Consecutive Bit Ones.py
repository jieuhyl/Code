# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:02:54 2020

@author: Jie.Hu
"""


# Consecutive Bit Ones

class solution(object):
    def maxconse(self,s):
        ans = 0
    
        while s != 0:
            s = (s&(s << 1))
            ans += 1
        return ans
print(solution().maxconse(242))