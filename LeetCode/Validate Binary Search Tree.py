# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:20:12 2020

@author: Jie.Hu
"""


#  Validate Binary Search Tree 

class solution(object):
    def validbst(self, node):
        def helper(node, low, high):
            if not node:
                return True
            
            val = node.val
            if val <= low or val >= high:
                return False
            if not helper(node.left, low, val):
                return False
            if not helper(node.right, val, high):
                return False
            return True
        return helper(node, float('-inf'), float('inf'))
