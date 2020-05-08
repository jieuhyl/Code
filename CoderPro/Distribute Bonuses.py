# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:51:54 2020

@author: Jie.Hu
"""



# Distribute Bonuses

class solution(object):
    def bonus(self, nums):
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                res[i] = res[i-1] + 1
        
        for j in range(len(nums)-2, -1, -1):
            if nums[j+1] < nums[j]:
                res[j] = max(res[j], res[j+1] + 1)
        
        return res

nums = [1, 2, 3, 1, 2, 3, 1]
print(solution().bonus(nums))