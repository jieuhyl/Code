# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:45:47 2020

@author: Jie.Hu
"""


# Find the non-duplicate number
nums = [4, 3, 2, 4, 1, 3, 2]


class solution(object):
    def find1(self, nums):
        dct = {}
        
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        
        for k, v in dct.items():
            if v%2 == 1:
                return k
            
    def find2(self, nums):
        uni = 0
        for num in nums:
            uni ^= num
        return uni
    
print(solution().find1(nums))
print(solution().find2(nums))