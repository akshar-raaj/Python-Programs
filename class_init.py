#!/usr/bin/python
#filename class_init.py
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        #print "Hello, I am "+self.name
        print ('Hello my name is {0}'.format(self.name))
Person("akshar").say_hi()