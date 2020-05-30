# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:36:15 2020

@author: Jie.Hu
"""


# Reverse A Linked List
class solution:
    def reverse(self, head):
        prev = nex = None
        cur = head
        
        while cur:
            nex = cur.next
            cur.next = prev
            
            prev, cur = cur, nex
        return prev