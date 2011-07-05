#!/usr/bin/python
#filename class_and_objects.py
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def set_name(self,name):
        self.name=name
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
"""p=Person("akshar")
p.set_name("shloka")
print p.get_name()"""
li=[]
p1=Person("abc",12)
p2=Person("def",15)
li.append(p1)
li.append(p2)
p=li[0]
print p.get_name()+" "+str(p.get_age())

        