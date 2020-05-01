# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:10:22 2020

@author: Jie.Hu
"""


# Roman Numerals to Decimal

romanNumerals = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class solution(object):
    def romanint(self, s):
        
        pre = 0
        ans = 0
        for i in s[::-1]:
            cur = romanNumerals[i]
            if cur >= pre:
                ans += cur
            else:
                ans -= cur
            pre = cur
        return ans

print(solution().romanint('MCMXCIV'))