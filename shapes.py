import math
class Shape:
   
    def calculate_area(self):
        pass
  
    def calculate_perimitor(self):
        pass



class Rectangle(Shape):
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calculate_area(self):
        area = self.height * self.width
        return area
    
    def calculate_perimitor(self):
        perimitor = 2 * self.height + 2 * self.width
        return perimitor

class Circle(Shape):
    
    def __init__(self, radius):
        
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius^2
        return area

    def calculate_perimitor(self):
        perimitor = 2 * math.pi * self.radius
        return perimitor
    

rect = Rectangle(10, 10)
print(rect.calculate_area())
print(rect.calculate_perimitor())

circ = Circle(1)
print(circ.calculate_area())
print(circ.calculate_perimitor())