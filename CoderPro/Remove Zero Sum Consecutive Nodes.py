# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:42:20 2020

@author: Jie.Hu
"""



# Remove Zero Sum Consecutive Nodes
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
        
class solution:
    def removezerosum(self, head):
        cur = dummy = Node(0)
        dummy.next = head
        s = 0
        dct = {}
        
        while cur:
            s += cur.val
            if s in dct:
                node = dct[s]
                node.next = cur.next
                while list(dct.keys())[-1] != s:
                    dct.popitem()
            else:
                dct[s] = cur
            cur = cur.next
        return dummy.next
    
    