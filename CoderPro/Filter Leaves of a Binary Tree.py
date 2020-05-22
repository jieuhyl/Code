# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:35:12 2020

@author: Jie.Hu
"""


# Filter Leaves of a Binary Tree

class solution():
    def filter(self, node, n):
        if not node:
            return None
        
        node.left = self.filter(node.left, n)
        node.right = self.filter(node.right, n)
        
        if node.val == n and not node.left and not node.right:
            return None
        return node
    
