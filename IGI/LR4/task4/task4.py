from abc import ABC, abstractmethod
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from inputvalidator import *

class GeometricShape(ABC):
    def __init__(self, color, name):
        self._color = ShapeColor(color)
        self._name = name

    def getShapeColor(self):
        return self._color

    color = property(getShapeColor)

    def getShapeName(self):
        return self._name

    name = property(getShapeName)

    @abstractmethod
    def calculate_area(self):
        pass

class ShapeColor:
    def __init__(self, color):
        self._color = color

    def getShapeColor(self):
        return self._color

    color = property(getShapeColor)

class Triangle(GeometricShape):
    def __init__(self, a, b, c, color, name):
        super().__init__(color, name)
        self._a = a
        self._b = b
        self._c = c 

    def getA(self):
        return self._a
    
    def getB(self):
        return self._b
        
    def getC(self):
        return self._c
    
    a = property(getA)
    b = property(getB)
    c = property(getC)

    def calculate_area(self):
        return round((self._a * self._b * np.sin(np.radians(self._c))) / 2, 1)
    
    def print_params(self):
        print("\033[1m Shape name: \033[00m {}\n\033[1m Shape Color: \033[00m {}\n\033[1m A side: \033[00m {}\n\033[1m B side: \033[00m {}\n\033[1m C angle between A n B: \033[00m {}\n\033[1m\033[92m Area: \033[00m {}"
              .format(self._name, self._color.color, self._a, self._b, self._c, self.calculate_area()))
        
class TriangleBuilder:
    def __init__(self, triangle: Triangle):
        self._triangle = triangle

    def build_triangle(self):
        c_ = np.radians(self._triangle.c)

        A = np.array([0, 0])
        C = np.array([self._triangle.a, 0])
        B = np.array([self._triangle.b * np.cos(c_), self._triangle.b * np.sin(c_)])


        plt.plot([A[0], C[0]], [A[1], C[1]], color='black')
        plt.plot([A[0], B[0]], [A[1], B[1]], color='black')
        plt.plot([B[0], C[0]], [B[1], C[1]], color='black')

        dots = np.array([A, B, C])

        hull = ConvexHull(dots)

        plt.fill(dots[hull.vertices, 0], dots[hull.vertices, 1], self._triangle.color.color)

        plt.axis('equal')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.title(self._triangle.name)
        figure = plt.gcf()
        figure.set_size_inches(9, 5)
        plt.savefig(r'C:\253504_Vilkina_4\IGI\LR4\task4\shape.png', dpi=300)
        plt.show()

class TaskFourth:
    @staticmethod
    def __call__():
        a = inputValidate("Enter A side: ", TYPES.INT)
        b = inputValidate("Enter B side: ", TYPES.INT)
        c = inputValidate("Enter angle between them: ", TYPES.INT)

        color = input('Enter color of triangle: ')
        name = input('Enter name of triangle: ')

        triangle = Triangle(a, b, c, color, name)
        triangle.print_params()

        builder = TriangleBuilder(triangle)
        builder.build_triangle()