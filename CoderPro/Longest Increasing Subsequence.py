# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:49:00 2020

@author: Jie.Hu
"""


# Longest Increasing Subsequence

class solution(object):
    def longest(self, nums):
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)
        return max(res)

nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(solution().longest(nums))