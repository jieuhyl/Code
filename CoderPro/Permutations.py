# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:25:57 2020

@author: Jie.Hu
"""

# permuatation

def permutation(nums):
    if len(nums) <= 1:
        return [nums]
    
    lst = []
    for idx, i in enumerate(nums):
        nums_rest = nums[:idx] + nums[idx+1:]
        for j in permutation(nums_rest):
            lst.append([i] + j)
    
    return lst

nums = ['a', 'b', 'c']
permutation(nums)
