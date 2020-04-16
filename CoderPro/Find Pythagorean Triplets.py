# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:02:19 2020

@author: Jie.Hu
"""


# Find Pythagorean Triplets

class solution(object):
    def findpt1(self, nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if a**2 + b**2 == c**2:
                        return True
        return False
    
    def findpt2(self, nums):
        nums2 = set([num**2 for num in nums])
        
        for a in nums:
            for b in nums:
                if a**2 + b**2 in nums2:
                    return True
        return False

print(solution().findpt1([1,4,5,2,12,13]))