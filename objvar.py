#!/usr/bin/python
#filename objvar.py
class Robot:
    
    population=0
    def __init__(self,name):
        self.__name=name
        print "Initializing {0}".format(self.__name)
        Robot.population+=1
        
    def say_hi(self):
        print "Greetings, my master calls me {0}".format(self.__name)
        
    def __del__(self):
        print "{0} is being destroyed".format(self.__name)
        Robot.population-=1
        if(Robot.population==0):
            print ("{0} was the last one ".format(self.__name))
        else:
            print ("There are still {0} robots left".format(Robot.population))
            
    def how_many():
        print "We have {0} robots left".format(Robot.population)
        
    how_many=staticmethod(how_many)

r1=Robot("R1")
r1.say_hi()
Robot.how_many()
r2=Robot("R2")
r2.say_hi()
Robot.how_many()
#print r1.name
del r1
del r2
Robot.how_many()
        
    