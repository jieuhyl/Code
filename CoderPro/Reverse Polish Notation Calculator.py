# -*- coding: utf-8 -*-
"""
Created on Wed May  6 01:15:25 2020

@author: Jie.Hu
"""


# Reverse Polish Notation Calculator

class solution(object):
    def reversepolish(self, nums):
        stack = []
        
        for i in nums:
            if i in ['+','-','*','/']:
              b = stack.pop()
              a = stack.pop()
              if i == '+':
                  stack.append(a+b)
              if i == '-':
                  stack.append(a-b)
              if i =='*':
                  stack.append(a*b)
              if i == '/':
                  stack.append(a/b)
            else:
                stack.append(i)
        return stack[0]
    
nums = [1, 2, 3, '+', 2, '*', '-']
print(solution().reversepolish(nums))
