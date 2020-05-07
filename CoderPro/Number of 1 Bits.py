# -*- coding: utf-8 -*-
"""
Created on Thu May  7 02:53:45 2020

@author: Jie.Hu
"""

# Number of 1 Bits

class solution(object):
    
    def numonebit(self, n):
        return bin(n).count('1')

print(solution().numonebit(23))