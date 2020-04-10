# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:05:41 2020

@author: Jie.Hu
"""


class Employee:
    
    num_of_emps = 0
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
   
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('a', 'b', 60000)     
emp_1.pay
emp_1.apply_raise()
emp_1.pay


print(Employee.num_of_emps)

print(emp_1.__dict__)
print(Employee.__dict__)


Employee.raise_amount = 1.1
emp_1.raise_amount
print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount = 1.2
emp_1.raise_amount
print(emp_1.__dict__)
print(Employee.__dict__)
