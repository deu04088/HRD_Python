import math
from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        
    def area(self):
        return self.__width * self.__height
    
    def get_diagonal(self):
        return math.sqrt(self.__width**2 + self.__height**2)