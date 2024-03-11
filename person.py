# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

	@abstractmethod
	def sides(self):
		pass


class Triangle(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 3 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 4 sides")


# Driver code
R = Triangle()
R.sides()

K = Quadrilateral()
K.sides()

