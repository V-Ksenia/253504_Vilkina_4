from sequenceinitialize import seqInputInit, seqRandomInit
from inputvalidator import inputValidate, TYPES
from decorator import funcInfoDec

@funcInfoDec
def calculateEven(list_):
    """Counts even numbers"""
    counter = 0

    for i in list_:
        if i % 2 == 0:
            counter += 1

    return counter


def task2():
    """Runs task2 \n
    Task: Create a loop that takes integers from the keyboard \\
    and counts the number of even numbers. \\
    End of cycle is entering a number greater than 1000
    """
    while True:

        choice = inputValidate("enter choice 1(user's input) or 2(random): ", TYPES.INT)

        match choice:
            case 1:
                list1 = seqInputInit()
                print(f"Amount of even numbers: {calculateEven(list1)}")
                return

            case 2:
                list2 = seqRandomInit()
                print(f"Amount of even numbers: {calculateEven(list2)}")
                return
            case _:
                print("Incorrect option")
                continue
