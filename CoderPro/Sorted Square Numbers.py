# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:38:39 2020

@author: Jie.Hu
"""

# Sorted Square Numbers

class solution(object):
    def sortedsquare1(self,nums):
        i = 0
        j = len(nums)-1
        res = []
        
        while i <= j:
            if nums[i]**2 <= nums[j]**2:
                res.append(nums[j]**2)
                j -= 1
            else:
                res.append(nums[i]**2)
                i += 1
        return res[::-1]
    
    def sortedsquare2(self, nums):
        neg_stack = []
        res = []
        for num in nums:
            if num < 0:
                neg_stack.append(num)
                continue
            while len(neg_stack) > 0 and neg_stack[-1]**2 <= num**2:
                res.append(neg_stack.pop()**2)
            res.append(num**2)
        return res
        
nums = [-5, -3, -1, 0, 1, 4, 5]
print(solution().sortedsquare2(nums))
        