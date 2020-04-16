# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:02:43 2020

@author: Jie.Hu
"""


# Product Of Array Except Self

class solution():
    def productes(self, nums):
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[i-1]*nums[i-1])
        
        right = 1
        for j in range(len(nums)-2, -1, -1):
            right *= nums[j+1]
            res[j] *= right
        return res

print(solution().productes([1,2,3,4]))