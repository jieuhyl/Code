# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:01:46 2020

@author: Jie.Hu
"""

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'shcarfer'
emp_1.email = 'cs@company.com'
emp_1.pay = 5000


emp_2.first = 'a'
emp_2.last = 'b'
emp_2.email = 'ab@company.com'
emp_2.pay = 6000


print(emp_1.first)


#=========================================
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    
emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('a', 'b', 60000)     

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_2.fullname())
print(Employee.fullname(emp_2))




