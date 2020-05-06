# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:08:11 2020

@author: Jie.Hu
"""


# Sum of Squares

class solution(object):     
    def sumsquares(self, n):
        lst = [n] * (n+1)
        lst[0] = 0
        lst[1] = 1
        
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                lst[i] = min(lst[i], lst[i-j*j] + 1)
                j += 1
        return lst[-1]

print(solution().sumsquares(13))