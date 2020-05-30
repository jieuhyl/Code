# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:13:40 2020

@author: Jie.Hu
"""


# Singly Linked List Cycle Check 

class solution:
    def cyclecheck(self, head):
        slow = fast = head
        
        while not slow and not fast:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False