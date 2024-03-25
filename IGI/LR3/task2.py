from sequenceinitialize import seqInputInit, seqRandomInit


def calculateEven(list_):

    counter = 0

    for i in list_:
        if i % 2 == 0:
            counter += 1

    return counter


def task2():
    while True:

        choice = int(input("enter choice 1(user's input) or 2(random): "))

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
                break
