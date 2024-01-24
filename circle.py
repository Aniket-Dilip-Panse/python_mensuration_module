class Circle:
  def __init__(self,radius):
    self.radius = radius
    self.pi = 3.14
  def area(self):
    return (self.pi * self.radius * self.radius)
  def circumference(self):
    return (2 * self.pi * self.radius)
