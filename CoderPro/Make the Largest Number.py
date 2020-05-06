# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:53:06 2020

@author: Jie.Hu
"""


# Make the Largest Number
from functools import cmp_to_key

class solution(object):
    def largestnum(self, nums):
        
        nums_str =[str(num) for num in sorted(nums, key = cmp_to_key(self.compare))]
        largest = ''.join(nums_str)
        return largest.lstrip('0') or '0'
    
        
    def compare(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return 1
        else:
            return -1
        
nums = [0,0]
nums = [17, 7, 2, 45, 72]
print(solution().largestnum(nums))