# -*- coding: utf-8 -*-
"""
Created on Tue May 19 01:40:43 2020

@author: Jie.Hu
"""


# Invert a Binary Tree

class solution():
    def invert(self, node):
        if not node:
            return None
        
        node.left, node.right = node.right, node.left
        
        self.invert(node.left)
        self.invert(node.right)
        
        return node
    