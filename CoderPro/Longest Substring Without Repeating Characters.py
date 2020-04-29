# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:31:00 2020

@author: Jie.Hu
"""


# Longest Substring Without Repeating Characters


class solution(object):
    def longsub(self, s):
        res = set()
        i = j = 0
        ans = 0
        
        while j < len(s):
            if s[j] not in res:
                res.add(s[j])
                ans = max(ans, j-i+1)
                j += 1
            else:
                res.remove(s[i])
                i += 1
        return ans

s = "abcabcbb"
s = ' '
print(solution().longsub(s))