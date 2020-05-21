# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:11:05 2020

@author: Jie.Hu
"""


# Balanced Binary Tree
class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    return self.val

#    a
#   / \
#  b   c
# /
# d
#  \
#   e
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.right = Node('c')

class solution:
    def balance(self, root):
        def _deep(node):
            if not node:
                return 0
            l = _deep(node.left)
            r = _deep(node.right)
            return max(l, r) + 1
    
        if not root:
            return True
        
        leftH = _deep(root.left)
        rightH = _deep(root.right)
        
        if abs(leftH - rightH) <= 1 and self.balance(root.left) is True and self.balance(root.right) is True:
            return True
        return False

print(solution().balance(root))
        