# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 01:00:40 2020

@author: Jie.Hu
"""

# 665. Non-decreasing Array
class solution(object):
    def checknon(self, nums):
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
    
print(solution().checknon([4,6,3]))
