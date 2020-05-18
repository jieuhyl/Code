# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:06:03 2020

@author: Jie.Hu
"""

# Trim a Binary Search Tree
class solution(object):
    def trim(self, node, minval, maxval):
        if not node:
            return 
        node.left = self.trim(node.left, minval, maxval)
        node.right = self.trim(node.right, minval, maxval)
        
        val = node.val
        if minval <= val <= maxval:
            return node
        if val < minval:
            return node.right
        if val > maxval:
            return node.left
        