# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:03:08 2020

@author: Jie.Hu
"""


# Remove Duplicate From Linked List
class solution:
    def remove(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
    