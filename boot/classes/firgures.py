from abc import ABC, abstractmethod
from math import pi, pow
import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.display.titles import title
from tools.display.text_align import left

# Declaracion interfaz
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Clase Circulo
class Circle(Figure):

    # Metodo constructor
    def __init__(self, radius: float):
        self.radius = radius

    # Calcular el area
    def area(self):
        return pi * (pow(self.radius, 2))

    # Calcular el perimetro
    def perimeter(self):
        return 2 * pi * self.radius
    
# Clase Rectangulo
class Rectangle(Figure):

    # Metodo constructor
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    # Calcular el area
    def area(self):
        return self.width * self.height

    # Calcular el perimetro
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Clase Triangulo
class Triangle(Figure):

    # Metodo constructor
    def __init__(self, base: float, height: float, side_a: float, side_b: float):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

    # Calcular el area
    def area(self):
        return (self.base * self.height) / 2

    # Calcular el perimetro
    def perimeter(self):
        return self.base + self.side_a + self.side_b

# Titulo
title("Figuras geometricas")

# Instanciar un objeto de tipo Circulo
circle = Circle(5)
print(left(f"Area del circulo: {circle.area()}",False))
print(left(f"Perimetro del circulo: {circle.perimeter()}",False), end="\n\n")

# Instanciar un objeto de tipo Rectangulo
rectangle = Rectangle(5, 10)
print(left(f"Area del rectangulo: {rectangle.area()}",False))
print(left(f"Perimetro del rectangulo: {rectangle.perimeter()}",False), end="\n\n")

# Instanciar un objeto de tipo Triangulo
triangle = Triangle(5, 10, 3, 4)
print(left(f"Area del triangulo: {triangle.area()}",False))
print(left(f"Perimetro del triangulo: {triangle.perimeter()}",False), end="\n\n")