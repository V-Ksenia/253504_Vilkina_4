from math import fabs
from inputvalidator import inputValidate, TYPES

lst = []

def listInputInit():
    size = inputValidate("Enter size of list: ", TYPES.INT)
    print("Enter list")
    for i in range(size):
        lst.append(inputValidate("", TYPES.INT))

def findMaxAbsoluteElement():
    maxElementIndex = 0
    for i in range(len(lst) - 1):
        if fabs(lst[i]) > fabs(lst[i + 1]):
            maxElementIndex = i
        else:
            maxElementIndex = i + 1
    return maxElementIndex


def multiplyElmentsBetweenZeros():
    result = 1.0
    for i in range(len(lst)):
        if lst[i] == 0:
            for j in range(i + 1, len(lst)):
                if lst[j] == 0:
                    return result
                result *= lst[j]
    return "No zero elements" 


def task5():
    listInputInit()
    print(f"max element index: {findMaxAbsoluteElement()}")
    print(f"result of multipluing list elements between zero elements: {multiplyElmentsBetweenZeros()}")
