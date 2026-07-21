#Task 5
import math
class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def __eq__(self, other):
       return self.x == other.x and self.y == other.y
       
    def __str__(self):
        return f'Point({self.x},{self.y})'
    
    def distance(self, other):
        return math.sqrt(((other.x - self.x)**2) + ((other.y - self.y)**2))
        
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f'Vector({self.x},{self.y})'

    def __add__(self, other):
       new_x = self.x + other.x
       new_y = self.y + other.y
       return Vector(new_x,new_y)
    
new_point = Point(3,2)
other_point = Point(4,3)
    
print(new_point == other_point)
print(new_point)
print(new_point.distance(other_point))

new_vector = Vector(3,5)
other_vector = Vector(2,3)

print(new_vector == other_vector)
print(new_vector)
print( new_vector + other_vector)