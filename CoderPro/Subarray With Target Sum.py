# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:04:52 2020

@author: Jie.Hu
"""


# Subarray With Target Sum

class solution(object):
    def subsum1(self, nums, k):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j]) == k:
                    return nums[i:j]
                
    def subsum2(self, nums, k):
        ans = 0
        dct = {}
        
        for idx, num in enumerate(nums):
            ans += num
            dct[ans] = idx
            if ans - k in dct:
                return (nums[dct[ans-k]+1:dct[ans]+1])
        return []
 
nums = [1, 3, 2, 5, 7, 2]
k = 14    
print(solution().subsum2(nums, k))