# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:41:15 2020

@author: Jie.Hu
"""


# Permutations

class solution:
    def permu(self, nums):
        res = []
        visit = set()
        
        def dfs(nums, cur):
            if len(cur) == len(nums):
                res.append(cur[:])
            for i in range(len(nums)):
                if i in visit:
                    continue
                visit.add(i)
                cur.append(nums[i])
                dfs(nums, cur)
                visit.remove(i)
                cur.pop()
        dfs(nums, [])
        return res

nums = [1,2,3]
print(solution().permu(nums))