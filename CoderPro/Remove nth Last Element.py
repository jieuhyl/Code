# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:54:27 2020

@author: Jie.Hu
"""


# Remove nth Last Element
class solution:
    def removenlast(self, head, n):
        dummy = Node(0)
        dummy.next = head
        slow = fast = dummy
        
        for i in range(n+1):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next