# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:00:22 2020

@author: Jie.Hu
"""

# Abosulte Paths

class solution(object):
    def clean_path(self, path):
        folder = path.split('/')
        res = []
        for f in folder:
            if f == '.':
                pass
            elif f == '..':
                res.pop()
            else:
                res.append(f)
        return '/'.join(res)

path = '/users/tech/docs/.././desk/../'
print(solution().clean_path(path))

