# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:52:11 2020

@author: Jie.Hu
"""


# Minimum Subarray Length

class solution(object):
    def minisub(self, nums, target):
        i = j = 0
        val = 0
        res = float('inf')
        
        while j < len(nums):
            val += nums[j]
            while val >= target:
                res = min(res, j-i+1)
                val -= nums[i]
                i += 1
            j += 1
        
        if res == float('inf'):
            return 0
        else:
            return res


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(solution().minisub(nums, target))