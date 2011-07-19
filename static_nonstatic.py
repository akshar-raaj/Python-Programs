class Person:
    #Static variable
    count=0
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print "Object created with "+self.name+" "+str(self.age)
        Person.increment_count()
        print "Count "+str(self.count)
    #Instance method    
    def get_name(self):
        return self.name
    
    #Static method
    def increment_count():
        Person.count=Person.count+1
        
    increment_count=staticmethod(increment_count)


p1=Person('abc',12)
p2=Person('def',16)