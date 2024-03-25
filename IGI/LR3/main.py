from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

while True:
    choice = input("Enter number from 1 to 5 or any other symbol to leave: \n")

    match choice:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case _:
            print("Program was finished")
            break