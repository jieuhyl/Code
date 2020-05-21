# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:09:05 2020

@author: Jie.Hu
"""


#  Maximum Depth of a Tree

class solution:
    def deep(self, root):
        if not root:
            return 0
        
        l = self.deep(root.left)
        r = self.deep(root.right)
        
        return max(l, r) + 1
    
    