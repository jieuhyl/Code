# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:26:16 2020

@author: Jie.Hu
"""


# Climbing Stairs

class solution(object):
    def climb1(self, n):
        if n <= 1:
            return 1
        else:
            return self.climb1(n-2) + self.climb1(n-1)
    
    def climb2(self, n):
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b
    
print(solution().climb1(8))