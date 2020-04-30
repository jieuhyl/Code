# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:20:05 2020

@author: Jie.Hu
"""


# Best Time to Buy and Sell Stock

class solution(object):
    def besttime(self, nums):
        if len(nums) < 2:
            return 0
        
        min_price = float('inf')
        max_price = 0
        
        for num in nums:
            min_price = min(min_price, num)
            max_price = max(max_price, num-min_price)
        return max_price

nums = [7,1,5,3,6,4]
print(solution().besttime(nums))