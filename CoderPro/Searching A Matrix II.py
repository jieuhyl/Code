# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:18:17 2020

@author: Jie.Hu
"""


# Searching A Matrix II
class solution:
    def searchmatrix(self, mtx, target):
        if len(mtx) == 0:
            return False
        m = len(mtx)
        n = len(mtx[0])
        currow = 0
        curcol = n-1
        while currow < m and curcol >= 0:
            print(mtx[currow][curcol])
            if mtx[currow][curcol] == target:
                return True
            elif mtx[currow][curcol] > target:
                curcol -= 1
            else:
                currow += 1
        return False

mtx = [[1, 4, 7, 11, 15],
       [2, 5, 8, 12, 19],
       [3, 6, 9, 16, 22],
       [10, 13, 14, 17, 24],
       [18, 21, 23, 26, 30]]
target = 13
print(solution().searchmatrix(mtx, target))