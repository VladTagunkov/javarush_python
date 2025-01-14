# Фигуры.

# Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от Shape
# и переопределять метод area для вычисления площади прямоугольника и круга соответственно.



import math

class Shape:
    def area(self):
        pass

# Напишите тут ваш код
class Rectangle(Shape):
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2 
        
    def area(self):
        return self.s1 * self.s2

class Circle(Shape):
    def __init__(self,r1):
        self.r1 = r1
        
    def area(self):
        return math.pi * (self.r1**2)



# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")