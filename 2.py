class Login:
	def __init__(self):
		self.__password = 123

	def get(self):
		return self.__password

	def set(self):
		self.__password = 456

# Creating a derived class
class Student(Login):
	def __init__(self):
		Login.__init__(self)
		self.set()
		print("Calling protected member of base class: ", self.get())
		#self._a = 3
		#print("Calling modified protected member outside class: ", self._a)


obj1 = Student()

#obj2 = Login()

# Calling protected member
# Can be accessed but should not be done due to convention
#print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
#print("Accessing protected member of obj2: ", obj2._a)



