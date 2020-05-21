# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:33:53 2020

@author: Jie.Hu
"""



# Clone Trees
from collections import deque
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.val)


class solution:
    def clone1(self, p, q, node):
        if p == node:
            return q
        
        if p.left and q.left:
            found = self.clone1(p.left, q.left, node)
            if found:
                return found
        if p.right and q.right:
            found = self.clone1(p.right, q.right, node)
            if found:
                return found
        return None
    
    
    def clone2(self, p, q, node):
        queue = deque([(p, q)])
        while queue:
            (p, q) = queue.popleft()
            if p == node:
                return q
            if p.left and q.left:
                queue.append((p.left, p.left))
            if p.right and q.right:
                queue.append((p.right, q.right))
        return None
    
#  1
# / \
#2   3
#   / \
#  4*  5
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.right.left = Node(4)
a.right.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.right.left = Node(4)
b.right.right = Node(5)

print(solution().clone2(a, b, a.right.left))
# 4    