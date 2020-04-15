# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:46:08 2020

@author: Jie.Hu
"""


# Queue Reconstruction By Height

nums = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

def queue(nums):
    nums = sorted(nums, key = lambda x: (-x[0], x[1]))
    
    res = []
    for num in nums:
        res.insert(num[1], num)
    return res

queue(nums)