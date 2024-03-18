from abc import ABC, abstractmethod

# (Interface Strategy)
class ShapeAreaCalculator(ABC):
  @abstractmethod
  def calculate_area(self):
    pass

# Concrete Strategies
class SquareAreaCalculator(ShapeAreaCalculator):
  def __init__(self, side):
    self.side = side

  def calculate_area(self):
    return self.side * self.side

class CircleAreaCalculator(ShapeAreaCalculator):
  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return 3.14159 * self.radius * self.radius

# Context
class Shape:
  def __init__(self, area_calculator):
    self.area_calculator = area_calculator

  def get_area(self):
    return self.area_calculator.calculate_area()

# Usage
# HR = ModelType(HR(data))
square = Shape(SquareAreaCalculator(5))
print("Square Area:", square.get_area())

circle = Shape(CircleAreaCalculator(3))
print("Circle Area:", circle.get_area())
