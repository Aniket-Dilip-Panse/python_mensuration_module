def triangle_perimeter(side1,side2,side3):
    return side1+side2+side3
def square_perimeter(side):
    return 4*side
def rectangle_perimeter(length,breadth):
    return 2 * (length+breadth)
def parallelogram_perimeter(side1,side2,side3,side4):
    '''Enter side1,side2,side3,side4 as a parameter'''
    return side1+side2+side3+side4
def rhombus_perimeter(side):
    '''Enter side of a rohmbus as a parameter'''
    return 4*side
def trapezium_perimeter(side1,side2,side3,side4):
    '''Enter side1,side2,side3,side4 as a parameter'''
    return side1+side2+side3+side4
def circle_perimeter(radius):
    '''Enter radius of circle as a parameter'''
    return 2 * 3.142 * radius
def equilateral_triangle_perimeter(side):
    '''Enter side of equilateral triangle as a parameter'''
    return 3 * side
def semicircle_perimeter(radius):
    '''Enter radius of circle as a parameter'''
    return (3.142 * radius) + (2 * radius)
def right_triangle_perimeter(side1,side2,hypotenuse):
    '''Enter side1 side2 and hypotenuse side as a parameter'''
    return side1 + side2 + hypotenuse
def isosceles_right_triangle_perimeter(side,hypotenuse):
    '''Enter side and hypotenuse side as a parameter'''
    return 2*side + hypotenuse