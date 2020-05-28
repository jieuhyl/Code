# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:55:07 2020

@author: Jie.Hu
"""


# Merge K Sorted Linked Lists

class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        

class solution:
    def mergek(lists):
        arr = []
        for i in lists:
            if i:
                arr.append(i.val)
        
        dummy = cur = Node(0)
        for val in sorted(arr):
            cur.next = Node(val)
            cur = cur.next
        return dummy.next