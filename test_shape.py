from shape.rectangle import Rectangle
from shape.circle import Circle

def printArea(shape):
    if type(shape) == Rectangle:
        s = 'rectangle\t'
        s += f'diagonal : {shape.get_diagonal():.2f}'
    elif type(shape) == Circle:
        s = 'circle\t'
        s += f'circumference : {shape.get_circummference():.2f}'
    else:
        pass
    print(s, '\tarea :', shape.area())
    
    
    
shapes = [
    Rectangle(10, 10, 5, 20), Circle(50, 50, 5), Rectangle(0, 0, 100, 5), Rectangle(50, 50, 5, 20)
]

for shape in shapes:
    printArea(shape)
