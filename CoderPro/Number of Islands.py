# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:48:27 2020

@author: Jie.Hu
"""


import collections            
                               
class solution(object):
    
    def numisland(self, mtx):
        if not mtx or len(mtx) == 0:
            return 0
        
        row = len(mtx)
        col = len(mtx[0])
        di = [[0,1], [0,-1], [1,0], [-1,0]]
        res = 0
        
        for i in range(row):
            for j in range(col):
                if mtx[i][j] == 1:
                    self.dfs(mtx, i, j, di)
                    res += 1
        return res
    
    def bfs(self, mtx, i, j, di):
        row = len(mtx)
        col = len(mtx[0])
        mtx[i][j] = '$'
        queue = collections.deque() #deck two way queue
        queue.append((i,j))
        
        while queue:
            currow, curcol = queue.popleft()
            for d in di:
                newrow = currow + d[0]
                newcol = curcol + d[1]
                if newrow >= 0 and newrow < row and newcol >= 0 and newcol< col and mtx[newrow][newcol] == 1:
                    mtx[newrow][newcol] = '$'
                    queue.append((newrow, newcol))
        
        
    def dfs(self, mtx,i,j,di):
        row = len(mtx)
        col = len(mtx[0])
        mtx[i][j] = '$'
        for d in di:
            newrow = i+d[0]
            newcol = j+d[1]
            if newrow >= 0 and newrow < row and newcol >= 0 and newcol < col and mtx[newrow][newcol] == 1:
                self.dfs(mtx,newrow,newcol,di)                
                    
        
mtx = [[1,1,1,0,0],
       [1,1,0,0,0],
       [0,0,1,0,0],
       [0,0,0,1,1]]

print(solution().numisland(mtx))     