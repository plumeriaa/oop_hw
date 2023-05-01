"""
Shape 클래스를 만들어서
-get_area 메소드를 갖게 해주세요.

Circle과 Rectangle 클래스를 Shape을 상속받아 만들어 주세요.
-Circle은 radius 속성을 가지게
-Rectangle은 length와 width 속성을 가지게
-get_area 메소드는 각각 맞게 구현해주세요.
"""

class Shape:
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14 * (self.radius**2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width 
    
circle = Circle(10)
print(circle.get_area())

rectangle = Rectangle(4,8)
print(rectangle.get_area())