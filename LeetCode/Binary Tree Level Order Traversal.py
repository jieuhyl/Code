# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:15:39 2020

@author: Jie.Hu
"""


# Binary Tree Level Order Traversal    
from collections import deque
class solution(object):
    def levelorder(self, node):
        if not node:
            return 
        
        res = []
        dq = deque([node])
        while dq:
            cur = []
            for i in range(len(dq)):
                node = dq.popleft()
                cur.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(cur)
        return res

    
    
    
    
    
    
    
    
    
    
    
    
      