# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:33:09 2020

@author: Jie.Hu
"""



# Valid Palindrome II

class solution(object):
    def valid(self, s):
        i = 0
        j = len(s)-1
        ispali = lambda x: x == x[::-1]
        
        while i < j:
            if s[i] != s[j]:
                return ispali(s[i:j]) or ispali(s[i+1:j+1])
            i += 1
            j -= 1
        return True

s = "aba"
print(solution().valid(s))