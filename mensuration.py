class Mensuration:
    class Triangle:
        def __int__(self):
            self.triangle_area()
            self.triangle_perimeter()
        def triangle_area(self,base,height):
            self.base = float(base)
            self.height = float(height)
            self.area = 0.5 * self.base * self.height
            print(f"Area of triangle with base = {self.base} and height = {self.height} is {self.area}")
        def triangle_perimeter(self,side1,side2,side3):
            self.side1 = float(side1)
            self.side2 = float(side2)
            self.side3 = float(side3)
            self.perimeter = self.side1 + self.side2 + self.side3
            print(f"perimeter of triangle with side1 = {self.side1}, side2 = {self.side2}, side3 = {self.side3} is {self.perimeter}")
    class square:
        def __init__(self):
            self.square_area()
        def square_area(self,side):
            self.side = float(side)
            self.area = self.side * self.side
            print(f"The area of square with side = {self.side} is {self.area}")
        def square_perimeter(self,side):
            self.side = float(side)
            self.perimeter = 4 * self.side
            print(f"The perimeter of square with side = {self.side} is {self.perimeter}")



            