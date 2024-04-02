from math import fabs, log
from decorator import funcInfoDec
from inputvalidator import inputValidate, TYPES

@funcInfoDec
def calculateSeries(x, eps):
    """Calculates ln(1-x) series"""

    result = 0.0
    for n in range(1, 500):
        result += (-1) * x**n / n
        if fabs(result - log(1 - x)) <= eps:
            print(f"x = {x}, n = {n}, ln(1-x) = {result}, math ln(1-x) = {log(1 - x)}, eps = {eps}")
            return n
    print("iterations > 500")
    return None

def task1():
    """Runs task1 \n
    Task: Calculate function values by expanding this function into a series \\
    Max iterations = 500 \\
    Print the number of series terms required to achieve the specified accuracy
    """
    while True:        
        x = inputValidate("enter x: ", TYPES.FLOAT)
        if fabs(x) > 1:
            print("|x| > 1. Enter again.")
        else:
            eps = inputValidate("enter eps: ", TYPES.FLOAT)
            calculateSeries(x, eps)
            return


    