# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:24:46 2020

@author: Jie.Hu
"""


# Best Time to Buy and Sell Stock II

class solution(object):
    def besttime(self, nums):
        if len(nums) < 2:
            return 0
        
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                ans += nums[i] - nums[i-1]
        return ans

nums = [7,1,5,3,6,4]
print(solution().besttime(nums))