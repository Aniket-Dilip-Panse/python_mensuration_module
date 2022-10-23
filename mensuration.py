class Mensuration:
    def __int__(self):
        self.triangle_area()
    def triangle_area(self,base,height):
        self.base = float(base)
        self.height = float(height)
        self.area = 0.5 * self.base * self.height
        print(f"Area of triangle with base = {self.base} and height = {self.height} is {self.area}")
triangle = Mensuration()
triangle.triangle_area(2,3)