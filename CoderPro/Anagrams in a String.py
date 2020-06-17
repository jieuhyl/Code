# -*- coding: utf-8 -*-
"""
Created on Sat May  2 02:04:50 2020

@author: Jie.Hu
"""

# Anagrams in a String
from collections import Counter
class solution(object):

    def findana(s, p):
        ans = []    
        dct_p = Counter(p)
        dct_s = Counter(s[:len(p)])

        if dct_p == dct_s:
            ans.append(0)

        for i in range(len(p), len(s)):
            dct_s[s[i]] += 1
            dct_s[s[i-len(p)]] -= 1
            if dct_s[s[i-len(p)]] == 0:
                del dct_s[s[i-len(p)]]
            #print(dct_s)
            if dct_s == dct_p:
                ans.append(i-len(p)+1)
        return ans

s = "cbaebabacd"
p = "abc"
print(solution().findana(s, p))
