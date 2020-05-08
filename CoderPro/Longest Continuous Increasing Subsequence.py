# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:43:41 2020

@author: Jie.Hu
"""



# Longest Continuous Increasing Subsequence

class solution(object):
    def longest(self, nums):
        idx = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                idx = i
            ans = max(ans, i-idx+1)
        return ans

nums = [1,3,5,4,7]
print(solution().longest(nums))