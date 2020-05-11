# -*- coding: utf-8 -*-
"""
Created on Mon May 11 02:56:42 2020

@author: Jie.Hu
"""


# Majority Element 

class solution(object):
    def major1(self, nums):
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
            if dct[num] > len(nums)/2:
                return num
    
    def major2(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    def major3(self, nums):
        cnt = 0
        idx = None
        for num in nums:
            if cnt == 0:
                idx = num
            if num == idx:
                cnt += 1
            else:
                cnt -= 1
        return idx

nums = [3, 5, 3, 3, 2, 4, 3]
print(solution().major3(nums))