# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:35:06 2020

@author: Jie.Hu
"""


# add two numbers
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class solution:
    def addtwo(self, l1, l2):
        def helper(a, b, c):
            if not a and not b and not c:
                return None
            a_val = a.val if a else 0
            b_val = b.val if b else 0
            tot = a_val+b_val+c
            
            a_next = a.next if a else None
            b_next = b.next if b else None
            c_next = 1 if tot >= 10 else 0
            
            return Node(tot%10, helper(a_next, b_next, c_next))
        return helper(l1, l2, 0)


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

print(solution().addtwo(l1, l2))
