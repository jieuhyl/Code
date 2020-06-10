# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:38:46 2020

@author: Jie.Hu
"""


# Sort Colors

class solution(object):
    def sortcolor1(self, nums):
        dct = {}
        
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        
        return [0]*dct.get(0) + [1]*dct.get(1) + [2]*dct.get(2)
    
    def sortcolor2(self, nums):
        p0 = 0
        p1 = 0
        p2 = len(nums)-1
        
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 1:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
        return nums
    
nums = [2,0,2,1,1,0]
print(solution().sortcolor2(nums))
