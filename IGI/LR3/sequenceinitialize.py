from random import randint
from inputvalidator import inputValidate, TYPES
from decorator import funcInfoDec

def seqRandomInit():

    seqSize = randint(5, 101)

    sequence = []

    for i in range(seqSize):
        sequence.append(randint(0, 1001))

    print(f"Random sequence: {sequence}")

    return sequence
    
@funcInfoDec
def seqGenerateInit():
    """Generator for random sequence input"""
    seqSize = randint(5, 101)

    for i in range(seqSize):
        i = randint(0, 1010)
        yield i

@funcInfoDec
def seqInputInit():
    """Function for user's sequence input"""
    print("Enter sequence: ")

    sequence = []

    while True:
        x = inputValidate("", TYPES.INT)
        
        if x > 1000:
            return sequence
        else:
            sequence.append(x)



        


