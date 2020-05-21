# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:43:00 2020

@author: Jie.Hu
"""


# Level by Level Trees
from collections import deque

class Node(object):
  def __init__(self, val, children):
    self.val = val
    self.children = children


class solution:
    def level(self, root):
        if not root:
            return None
        
        res = []
        queue = deque([root])
        while queue:
            cur = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                for j in node.children:
                    queue.append(j)
            res.append(cur)
        return res


tree = Node('a', [])
tree.children = [Node('b', []), Node('c', [])]
tree.children[0].children = [Node('g', [])]
tree.children[1].children = [Node('d', []), Node('e', []), Node('f', [])]

print(solution().level(tree))