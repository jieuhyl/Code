# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:28:47 2020

@author: Jie.Hu
"""

# Closest Points to the Origin

import heapq

class solution(object):
    def caldist(self, p):
        return p[0]**2 + p[1]**2
    
    def findtopk1(self, points, k):
        points.sort(key = lambda x: self.caldist(x))
        return points[:k]
    
    def findtopk2(self, points, k):
        heap = []
        for p in points:
            heapq.heappush(heap, (self.caldist(p)*-1, p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [j for (i,j) in heap]
    
    def findtopk3(self, points, k):
        lst = []
        for p in points:
            lst.append((self.caldist(p), p))
        heapq.heapify(lst)
        
        res = heapq.nsmallest(k, lst)
        return [j for (i,j) in res]


points = [[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]]
k = 3

print(solution().findtopk2(points, k))