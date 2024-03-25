from math import fabs, log

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
    x = float(input("enter x: "))
    eps = float(input("enter eps: "))

    calculateSeries(x, eps)

    return


    