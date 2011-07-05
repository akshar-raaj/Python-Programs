class SchoolMember:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print "Initializing school member {0}".format(self.name)

	def tell(self):
		print "Name: {0} Age: {1}".format(self.name,self.age)

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print "Initialaizing teacher {0}".format(self.name)

	"""def tell(self):
		SchoolMember.tell(self)
		print "{0} salary is {1}".format(self.name,self.salary)"""

s=SchoolMember("abc",30)
s.tell()
t=Teacher("def",50,100000)
t.tell()
