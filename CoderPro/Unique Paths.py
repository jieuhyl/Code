# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:48:25 2020

@author: Jie.Hu
"""


# Unique Paths

class solution(object):
    def uniquepath(self, m, n):
        
        mtx = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            mtx[i][0] = 1
        for j in range(n):
            mtx[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                mtx[i][j] = mtx[i-1][j] + mtx[i][j-1]
                
        return mtx[-1][-1]
    
print(solution().uniquepath(3,7))