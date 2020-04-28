# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:48:53 2020

@author: Jie.Hu
"""


# Maximum Subarray 


class solution(object):
    def maxsub(self, nums):
        
        last = cur = float('-inf')
        
        for num in nums:
            last = max(num, last+num)
            cur = max(cur, last)
        return cur

nums = [-1, -4, 3, 8, 1]
print(solution().maxsub(nums))