# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:38:35 2020

@author: Jie.Hu
"""


# Merge Intervals

class solution(object):
    def mergeintervals(self, intervals):
        intervals.sort(key = lambda x:x[0])
        res = []
        
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

intervals = [[1, 5], [10, 12],[2, 8]]
print(solution().mergeintervals(intervals))