# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:30:03 2020

@author: Jie.Hu
"""


# subtree

class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
        
class solution:
    def subtree(self, s, t):
        def preorder(node):
            if not node:
                return '#'
            return '^' + str(node.val) + '$' + preorder(node.left) + preorder(node.right)
        return preorder(t) in preorder(s)
   
s3 = Node(4, Node(3), Node(2))
s2 = Node(5, Node(4), Node(-1))
s = Node(1, s2, s3)

t = Node(4, Node(3), Node(2))

print(solution().subtree(s, t)) 