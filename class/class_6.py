# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:30:29 2020

@author: Jie.Hu
"""


class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
emp_1 = Employee('corey', 'schafer', 50000)

emp_1.fullname = 'a b'

print(emp_1.first)
print(emp_1.fullname)

del emp_1.fullname

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


