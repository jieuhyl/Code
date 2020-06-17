# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:37:01 2020

@author: Jie.Hu
"""


# Searching A Matrix
class solution:
    def searchmtx(self, mtx, target):
        m = len(mtx)
        n = len(mtx[0])
        low = 0
        high = m*n
        
        while low <= high:
            mid = (low + high)//2
            if mtx[mid//n][mid%n] == target:
                return True
            elif mtx[mid//n][mid%n] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

mtx = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]
target = 15
print(solution().searchmtx(mtx, target))