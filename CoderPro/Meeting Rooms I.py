# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 00:49:29 2020

@author: Jie.Hu
"""

# 252. Meeting Rooms

class solution(object):
    
    def meetingroom(self, intervals):
        if len(intervals) == 0:
            return True
        
        intervals.sort(key = lambda x: x[0])
        
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True

intervals =  [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]

print(solution().meetingroom(intervals))
                





