# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:16:19 2020

@author: Jie.Hu
"""


import heapq

# Find the Kth Largest Element in a List
class solution(object):
    def findk1(self, nums, k):
        nums = sorted(nums, reverse = True)
        return nums[k-1]
    
    def findk2(self, nums, k):
        nums = sorted(nums)
        return nums[len(nums)-k]
    
    def findk3(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

nums = [3, 1, 5, 2, 4, 6, 8]
k = 3
print(solution().findk3(nums, k))
