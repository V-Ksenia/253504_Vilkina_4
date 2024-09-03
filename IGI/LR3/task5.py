from math import fabs
from decorator import funcInfoDec
from inputvalidator import inputValidate, TYPES


@funcInfoDec
def listInputInit():
    """Initializes list from user's input"""
    lst_ = []
    size = inputValidate("Enter size of list: ", TYPES.INT)

    if size <= 0:
        print("List is empty: ")
        return lst_
    
    print("Enter list: ")
    for i in range(size):
        lst_.append(inputValidate("", TYPES.FLOAT))
    return lst_

@funcInfoDec
def findMaxAbsoluteElement(lst):
    """Returns index of max element"""
    maxElementIndex = 0
    for i in range(len(lst)):
        if fabs(lst[maxElementIndex]) < fabs(lst[i]):
            maxElementIndex = i
    return maxElementIndex

@funcInfoDec
def multiplyElementsBetweenZeros(lst):
    """Multiplies elements between first and second zeros in sting"""
    result = 1.0
    c = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            for j in range(i + 1, len(lst)):
                if lst[j] == 0:
                    if c == 0:
                        return 0.0
                    return result
                result *= lst[j]
                c += 1
    
    return "No zero elements" 

@funcInfoDec
def task5():
    """Runs task5 \n
    Task: Find the number of the maximum modulo element of the list and   
    the product of the elements located between the first and second zero element.
    """
    llist = listInputInit()
    print(f"List: {llist}")
    print(f"Max element index: {findMaxAbsoluteElement(llist)}")
    print(f"Result of multipluing list elements between zero elements: {multiplyElementsBetweenZeros(llist)}")
