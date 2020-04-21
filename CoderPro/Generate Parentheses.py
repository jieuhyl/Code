# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:19:52 2020

@author: Jie.Hu
"""


# Generate Parentheses

class solution(object):
    def generatepar(self, n):
        
        res = []
        
        def backtrack(s, left, right):
            if len(s) == 2*n:
                res.append(s)
                return            
            if left < n:
                backtrack(s+'(', left+1, right)                
            if left > right:
                backtrack(s+')', left, right+1)
        
        backtrack('', 0, 0)
        return res

n = 3
print(solution().generatepar(n))



        