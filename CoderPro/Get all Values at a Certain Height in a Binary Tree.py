# -*- coding: utf-8 -*-
"""
Created on Mon May 25 02:56:43 2020

@author: Jie.Hu
"""


# Get all Values at a Certain Height in a Binary Tree
class Node():
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

#    1
#   / \
#  2   3
# / \   \
# 4   5   7
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)
k = 3

class solution:
    def getval(self, root, k):
        if not root:
            return None
        
        queue = [root]
        cnt = 0
        while queue:
            cur = []
            for i in range(len(queue)):
                node = queue.pop(0)
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cnt += 1
            if cnt == k:
                return cur
print(solution().getval(node, k))