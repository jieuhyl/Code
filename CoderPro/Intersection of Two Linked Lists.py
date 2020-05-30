# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:59:04 2020

@author: Jie.Hu
"""


# Intersection of Two Linked Lists  
class solution:
    def intersect(self, headA, headB):
        a = headA
        b = headB
        
        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        return a