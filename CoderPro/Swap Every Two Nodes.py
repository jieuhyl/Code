# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:31:31 2020

@author: Jie.Hu
"""


# Swap Every Two Nodes
class solution:
    def swap(self, head):
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next
        return head
    
