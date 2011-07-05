class Person:
	age=12
	def __init__(self,name):
		self.name=name
	def say_hi(self):
		print self.name, self.age
	def print_age():
		print Person.age
	print_age=staticmethod(print_age)
p=Person("def")
p2=Person("newPerson")
p.say_hi()
p2.say_hi()
Person.print_age()
