import os
from task1.task1 import TaskFirst
from task3.task3 import TaskThird
from task4.task4 import TaskFourth
from task5.task5 import TaskFifth
#   -----LAB №4. .-----
#   Made by Ksenia Vilkina. Gr.253504
#   12.04.2024


while True:
    choice = input("\n \033[1m ENTER NUMBER FROM 1 TO 5 OR ANY OTHER SYMBOL TO LEAVE: \033[00m \n")

    match choice:
        case "1":
            task1 = TaskFirst()
            task1()
        case "2":
            pass
           # task2()
        case "3":
            task3 = TaskThird()
            task3()
        case "4":
            task4 = TaskFourth()
            task4()
        case "5":
            task5 = TaskFifth()
            task5()
        case _:
            os.system("cls")
            print("\033[96m \033[1m Program was finished \033[00m")
            break


