# -*- coding: utf-8 -*-
"""
Created on Sat May 30 03:05:15 2020

@author: Jie.Hu
"""


# Remove Duplicates from Sorted List II
class solution:
    def remove(self, head):
        dummy = Node(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next