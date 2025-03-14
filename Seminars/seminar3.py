# Task 1:
# Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter.
# Использовать библиотеку абстрактных классов “ABC” в данном случае - не обязательно.
import math


class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


# Task 2:
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
#   ○ конструктор класса __init__ - метод инициализации класса Circle.
#   ○ get_area - метод для расчета площади круга
#   ○ get_perimeter - метод для расчета периметра окружности

class Circle(Shape):    # унаследовали от Shape
    def __init__(self, radius):     # конструктор класса с переменной radius
        self.radius = radius

    def get_area(self):             # переопределяем методы родительского класса
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius


# Task 3:
# Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
#   ○ конструктор класса __init__ - метод инициализации класса.
#   ○ get_area - метод для расчета площади
#   ○ get_perimeter - метод для расчета периметра

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = self.get_perimeter() / 2
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c