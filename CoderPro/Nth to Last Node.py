# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:39:00 2020

@author: Jie.Hu
"""


# Nth to Last Node
class solution:
    def nlast(self, head, n):
        slow = fast = head
        
        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow