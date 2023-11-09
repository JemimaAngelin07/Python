import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def cal_area_circle(self):
        return math.pi * self.radius ** 2
    def cal_circle_perimeter(self):
        return 2 * math.pi * self.radius
radius=float(input("Enter a Radius Value:"))
result=Circle(radius)   
area=result.cal_area_circle()
perimeter=result.cal_circle_perimeter()
print("Area of Circle :",area)
print("Perimeter of Circle:",perimeter) 