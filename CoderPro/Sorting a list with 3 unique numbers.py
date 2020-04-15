# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:46:29 2020

@author: Jie.Hu
"""


# Sorting a list with 3 unique numbers
nums = [3, 3, 2, 1, 3, 2, 1]
def sortlist(nums):
    dct = {}
    for num in nums:
        dct[num] = dct.get(num,0) + 1
    return ([1] * dct.get(1, 0) + [2] * dct.get(2, 0) + [3] * dct.get(3 ,0))
sortlist(nums)


def sortlist2(nums):
    dct = {}
    for i in nums:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

    return ([1] * dct.get(1) + [2] * dct.get(2) + [3] * dct.get(3))

sortlist2(nums)


def sortlist3(nums):
    dct = {}
    for i in nums:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    
    dct = dict(sorted(dct.items(), key = lambda x: x[0]))
    
    res = []
    for k, v in dct.items():
        res.extend([k]*v)
    return res

sortlist3(nums)



nums = [3, 3, 2, 1, 3, 2, 1]
def sortlist4(nums):
    low = 0
    high = len(nums) - 1
    idx = 0
    
    while idx <= high:
        #print(nums)
        if nums[idx] == 1:
            nums[idx], nums[low] = nums[low], nums[idx]
            low += 1
            idx += 1
            print('first run is {} and index is {}'.format(nums, idx))
        elif nums[idx] == 2:
            idx += 1
            print('second run is {} and index is {}'.format(nums, idx))
        else:
            nums[idx], nums[high] = nums[high], nums[idx]
            high -= 1
            print('third run is {} and index is {}'.format(nums, idx))
    return nums
sortlist4(nums)