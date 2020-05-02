# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:27:09 2020

@author: Jie.Hu
"""


import re
# Valid Palindrome I

class solution(object):
    def valid1(self, s):
        pat = re.compile('\W')
        s = re.sub(pat, '', s).lower()
        
        i = 0
        j = len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def valid2(self, s):
        pat = re.compile('\W')
        s = re.sub(pat, '', s).lower()
        
        ispali = lambda x: x == x[::-1]
        return ispali(s)
 
s = "A man, a plan, a canal: Panama"
print(solution().valid1(s))