# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:58:05 2020

@author: Jie.Hu
"""


# Fixed Point

class solution(object):
    def fixpt1(self, nums):
        for idx, num in enumerate(nums):
            if idx == num:
                return num
        return -1
    
    def fixpt2(self, nums):
        i = 0
        j = len(nums)-1
        ans = None
        while i <= j and (nums[i]-i)*(nums[j]-j) <= 0:
            mid = (i+j)//2
            if nums[mid] == mid:
                ans = mid
            if nums[mid] < mid:
                i = mid + 1
            else:
                j = mid - 1
        return ans if ans is not None else -1

nums = [-10,-5,0,3,7]
print(solution().fixpt2(nums))