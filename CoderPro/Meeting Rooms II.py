# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:55:27 2020

@author: Jie.Hu
"""


# 253. Meeting Rooms II
import heapq

class solution(object):
    
    def meetingroom1(self, intervals):
        if len(intervals) == 0:
            return 0
        
        intervals.sort()
        
        dct = {}
        
        for interval in intervals:
            for i in range(interval[0], interval[1]):
                dct[i] = dct.get(i, 0) + 1
                
        return max(dct.values())
    
    
    def meetingroom2(self, intervals):
        if len(intervals) == 0:
            return 0
        
        intervals.sort()
        hp = []
        for interval in intervals:
            if not hp:
                heapq.heappush(hp,interval[1])
            else:
                if hp[0] <= interval[0]:
                    heapq.heappop(hp)
                heapq.heappush(hp, interval[1])
        return len(hp)

intervals =  [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
print(solution().meetingroom2(intervals))
