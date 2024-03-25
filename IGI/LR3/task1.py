from math import fabs, log
from inputvalidator import inputValidate, TYPES

def calculateSeries(x, eps):
    result = 0.0
    for n in range(1, 500):
        result += (-1) * x**n / n
        if fabs(result - log(1 - x)) <= eps:
            print(f"x = {x}, n = {n}, ln(1-x) = {result}, math ln(1-x) = {log(1 - x)}, eps = {eps}")
            return
    print("iterations > 500")
    return

def task1():
    while True:
        
        x = inputValidate("enter x: ", TYPES.FLOAT)
        if fabs(x) > 1:
            print("|x| > 1. Enter again.")
        else:
            eps = inputValidate("enter eps: ", TYPES.FLOAT)
            calculateSeries(x, eps)
            return


    