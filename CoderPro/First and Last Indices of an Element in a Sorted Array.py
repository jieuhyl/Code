# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:31:28 2020

@author: Jie.Hu
"""


# First and Last Indices of an Element in a Sorted Array
class solution:
    def getrange(self, nums, k):
        first = self.binarysearch(nums, 0, len(nums)-1, k, True)
        last = self.binarysearch(nums, 0, len(nums)-1, k, False)
        return [first, last]

    def binarysearch(self, nums, low, high, k, find):
        while True:
            if high < low:
                return -1
        
            mid = (low + high) // 2
            
            if find:
                if nums[mid] == k and (mid == 0 or k > nums[mid - 1]):
                    return mid
                elif k > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            else:
                if nums[mid] == k and (mid == len(nums) - 1 or k < nums[mid + 1]):
                    return mid
                elif k < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
nums = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
k = 9
print(solution().getrange(nums, k))    

            
            