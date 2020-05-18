# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:29:04 2020

@author: Jie.Hu
"""

    
# Combinations

class solution:
    def comb(self, nums, k):
        res = []
        def dfs(idx, cur):
            if len(cur) == k:
                res.append(cur[:])
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return res

nums = [1,2,3,4]
k = 2
print(solution().comb(nums, k))