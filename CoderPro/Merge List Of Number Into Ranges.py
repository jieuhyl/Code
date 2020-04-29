# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:34:27 2020

@author: Jie.Hu
"""


# Merge List Of Number Into Ranges

class solution(object):
    def mergelist(self, nums):
        
        res = []
        low = high = nums[0]
        
        for num in nums:
            if high + 1 < num:
                res.append((str(low) +'-'+ str(high)))
                low = num
            high = num
        res.append((str(low) +'-'+ str(high)))
        return res

nums = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
print(solution().mergelist(nums))
            