from random import randint

def seqRandomInit():

    seqSize = randint(5, 101)

    sequence = []

    for i in range(seqSize):
        sequence.append(randint(0, 1001))

    print(f"Random sequence: {sequence}")

    return sequence
    

def seqInputInit():

    print("Enter sequence: ")

    sequence = []

    while True:
        x = int(input())
        
        if x > 1000:
            return sequence
        else:
            sequence.append(x)



        


