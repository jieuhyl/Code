# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:20:37 2020

@author: Jie.Hu
"""

# two sum
nums = [2,7,11,15]
k = 9

def twosum(nums, k):
    dct = {}
    
    for idx, num in enumerate(nums):
        if k - num not in dct:
            dct[num] = idx
        else:
            return (dct[k-num], idx)
    return False
twosum(nums, k)
    
    
    
def twosum(nums, k):
    lst = set()
    for num in nums:
        if k - num in lst:
            return (num, k-num)
        lst.add(num)
    return False
twosum(nums, k)
    