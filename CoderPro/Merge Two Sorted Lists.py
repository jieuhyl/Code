# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:46:48 2020

@author: Jie.Hu
"""


# Merge Two Sorted Lists
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class solution:
    def mergetwo(self, l1, l2):
        dummy = cur = Node(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next