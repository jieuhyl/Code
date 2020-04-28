# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:56:58 2020

@author: Jie.Hu
"""


# Angles of a Clock

class solution(object):
    # min speed
    def angleclock(self, h, m):
        ang_h = 360/(12*60) * (h*60 + m)
        ang_m = 360/60 * m
        
        diff = abs(ang_h - ang_m)
        return min(diff, 360-diff)
    
    # hour speed
    def angleclock2(self, h, m):
        ang_h = 360/12*(h+m/60)
        ang_m = 360*(m/60)
        
        diff = abs(ang_h - ang_m)
        return min(diff, 360-diff)
    
print(solution().angleclock2(3,15))