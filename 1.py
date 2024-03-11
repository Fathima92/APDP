class Maths:
  institution = "BCAS"
  def __init__(self, name, id):
      self.name = name
      self.id = id
  def add(self, x,y):
      return x + y

  def sub(self, x, y):
      return  x-y

  def multiply(self, x, y):
      #print(self.name, self.id)
      return x * y

class Student(Maths):
    pass
def name(self, name, id):
 print(self.name, self.id)


obj1 = Maths("ABC", "1")
obj2 = Maths("XYZ", "2")
print(obj1.multiply(5,7))



