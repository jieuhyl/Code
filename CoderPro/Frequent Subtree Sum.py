# -*- coding: utf-8 -*-
"""
Created on Sun May 24 03:00:51 2020

@author: Jie.Hu
"""


## Frequent Subtree Sum

class Node():
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

root = Node(4)  
root.left = Node(1)  
root.left.left = Node(2)
root.left.right = Node(3)
root.right = Node(-1)  
root.right.left = Node(4)
root.right.right = Node(5)

class solution:
    def freqsubsum(self, root):
        if not root:
            return None
    
        res = []
        def _subsum(node):
            if not node:
                return 0
            sub = _subsum(node.left) + node.val + _subsum(node.right)
            res.append(sub)
            return sub
        
        _subsum(root)
    
        dct = dict()
        for i in res:
            dct[i] = dct.get(i, 0) + 1
            
        freq_max = max(dct.values())
        
        ans = list()
        for i,j in dct.items():
            if j == freq_max:
                ans.append(i)
        return ans

print(solution().freqsubsum(root))