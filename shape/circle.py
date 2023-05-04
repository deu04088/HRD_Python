from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius
        
    def area(self):
        return 3.141952 * self.__radius**2
    
    def get_circummference(self):
        return 3.141952 * (self.__radius + self.__radius)