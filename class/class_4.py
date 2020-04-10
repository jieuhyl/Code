# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:10:42 2020

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
        self.pay = int(self.pay * self.raise_amt)
        
        
        
class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('corey', 'schafer', 50000, 'python')
dev_2 = Developer('a', 'b', 60000, 'java')  

mgr_1 = Manager('sue', 'smith', 100000, [dev_1])
print(mgr_1.email)

mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))



print(dev_1.email)
print(dev_1.lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)