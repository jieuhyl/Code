# -*- coding: utf-8 -*-
"""
Created on Sat May  2 02:04:50 2020

@author: Jie.Hu
"""

# Anagrams in a String
from collections import Counter
class solution(object):

    def findAnagrams(self, s, p):
    
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n-1])
        print(pCounter)
        print(sCounter)
    
        index = 0
        for index in range(n - 1, m):
                sCounter[s[index]] += 1
                if sCounter == pCounter:
                    answer.append(index - n + 1)
                sCounter[s[index - n + 1]] -= 1
                if sCounter[s[index - n + 1]] == 0:
                    del sCounter[s[index - n + 1]]
        return answer

s = "cbaebabacd"
p = "abc"
print(solution().findAnagrams(s, p))