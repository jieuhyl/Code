# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:16:18 2020

@author: Jie.Hu
"""


# Longest Common Prefix

class solution(object):
    def longcom1(self, strs):
        
        if len(strs) == 0:
            return ''
    
        start = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(start, 0, len(start)):
                start = start[:-1]
        return start
    
    def longcom2(self, strs):
        strs.sort(key = len)
        #res = set()
        ans = ''
        for i in range(len(strs[0])):
            res = set()
            for s in strs[1:]:
                res.add(s[i])
            if len(res) == 1:
                ans += strs[0][i]
            else:
                return ans
        return ans
                
strs = ['daily', 'interview', 'pro']
strs = ['helloworld', 'hellokitty', 'hell']
print(solution().longcom2(strs))