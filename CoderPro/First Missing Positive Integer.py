# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:03:00 2020

@author: Jie.Hu
"""


# First Missing Positive Integer

class solution(object):
    
    def firstmissing(self, nums):
        
        dct = {}
        for num in nums:
            dct[num] = 1
        
        for i in range(1, len(nums)):
            if i not in dct:
                return i
        return -1

nums = [3,4,-1,1,1]
print(solution().firstmissing(nums))