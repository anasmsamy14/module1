import math

class Circle:
    
    def __init__(self, radius):
        self.radius = float(radius)

   
    def area(self):
        
        return math.pi * (self.radius ** 2)

  
    def perimeter(self):
     
        return 2 * math.pi * self.radius




user_input = input("Enter the radius of the circle: ")


my_circle = Circle(user_input)

print(f"\nFor a circle with radius {my_circle.radius}:")
print(f"Area: {my_circle.area():.2f}")
print(f"Perimeter: {my_circle.perimeter():.2f}")