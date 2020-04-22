# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:17:46 2020

@author: Jie.Hu
"""


# three sum

class solution(object):
    def threesome1(self, nums):
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res
    
    def threesome2(self, nums):
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res

nums = [-1,0,4,2,1,-1]
print(solution().threesome1(nums))