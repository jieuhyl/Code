# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:45:24 2020

@author: Jie.Hu
"""


# Subsets
class solution:
    def subset(self, nums):
        res = []
        def dfs(idx, cur):
            res.append(cur[:])
            for i in range(idx, len(nums)):
                cur.append(nums[i])
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return res

nums = [1,2,3]
print(solution().subset(nums))