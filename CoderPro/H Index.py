# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:05:18 2020

@author: Jie.Hu
"""


# H Index

class solution(object):
    def hindex1(self, nums):
        nums.sort(reverse = True)
        
        h = 0
        for idx, i in enumerate(nums):
            if idx + 1 <= i:
                h += 1
        return h
    
    def hindex2(self, nums):
        lst = [0] * len(nums)+1
        for num in nums:
            if num >= len(nums):
                lst[len(nums)] += 1
            else:
                lst[num] += 1
                
        h = 0
        i = len(nums)
        while i>=0:
            h += lst[i]
            if h >= i:
                return i
            i -= 1
        return i

nums = [5, 3, 3, 1, 0]
nums = [0,1]
print(solution().hindex1(nums))