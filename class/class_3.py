# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:31:14 2020

@author: Jie.Hu
"""

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.05
    
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
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        return day.weekday() not in [5, 6]
    
    
emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('a', 'b', 60000)  

Employee.set_raise_amt(1.1)

print(Employee.raise_amt)
print(emp_1.raise_amt)

emp_str_1 = 'a-b-50000'

emp_1 = Employee.from_string(emp_str_1)
print(emp_1.pay)

import datetime
my_date = datetime.date(2020, 4, 30)
print(Employee.is_workday(my_date))

