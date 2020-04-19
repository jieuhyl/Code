# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:10:00 2020

@author: Jie.Hu
"""


import collections
import heapq
# Top K Frequent Elements
class solution(object):
    def topk1(self, nums, k):
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        
        hp = []
        for key, val in dct.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        
        res = []
        for (i, j) in hp:
            res.append(j)
        
        return res
    
    def topk2(self, nums, k):
        dct = collections.Counter(nums)
        
        return heapq.nlargest(k, dct.keys(), key = dct.get)
 
    
nums = [1,1,1,2,2,3]
t = 2    
print(solution().topk2(nums, t))




