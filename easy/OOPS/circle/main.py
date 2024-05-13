# Write a  Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.14

    def calculate_area(self):    
        area = self.PI * (self.radius ** 2)
        return area

    def calculate_perimeter(self):
        perimeter = round((2 * self.PI * self.radius),2)
        return perimeter

my_circle = Circle(10)
print(my_circle.calculate_area())
print(my_circle.calculate_perimeter())