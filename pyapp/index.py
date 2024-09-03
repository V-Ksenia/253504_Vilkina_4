import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

def area2(a):
    return a * a

def perimeter2(a):
    return 4 * a


print("Circle area: ", area(3))
print("Circle perimeter: ", perimeter(3))

print("Square area: ", area2(4))
print("Square perimeter: ", perimeter2(4))

var1 = input()