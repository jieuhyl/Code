# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:27:13 2020

@author: Jie.Hu
"""


# Phone Numbers
lettersmap = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

def getlst(n):
    lst = []
    for i in str(n):
        lst.append(''.join(lettersmap[int(i)]))
    return lst
getlst(364)
        

def getcomb(lst):
    res = []
    def backtracking(cur, lst, idx):
        if len(cur) == len(lst):
            res.append(cur)
            return
        for i in range(idx, len(lst)):
            for j in lst[i]:
                cur += j
                backtracking(cur, lst, i+1)
                cur = cur[:-1]
    backtracking('', lst, 0)
    return res
getcomb(getlst(36))