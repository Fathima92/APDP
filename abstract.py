# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

class BCAS(ABC):
	@abstractmethod
	def fingure(self):
		pass
class Student(BCAS):
	# overriding abstract method
	def fingure(self):
		print("Student Fingure Time 8.30AM")
class Lecturer(BCAS):

	# overriding abstract method
	def fingure(self):
		print("Lecturer Fingure Time 8.00AM")

# Driver code
lec = Lecturer()
lec.fingure()

stu = Student()
stu.fingure()

#R = Pentagon()
#R.sides()

