# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:06:41 2020

@author: Jie.Hu
"""


# Count Univalue Subtrees
class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)


class solution:
    def countunisub(self, root):
        ans = []
        def _helper(node):
            if not node:
                return True
            
            isleft = _helper(node.left)
            isright = _helper(node.right)
            
            if isleft and isright and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
                ans.append(True)
                return True
            else:
                return False
        _helper(root)
        return len(ans)
print(solution().countunisub(a))