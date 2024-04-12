import os
from task1.task1 import TaskFirst

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
            pass
           # task3()
        case "4":
            pass
           # task4()
        case "5":
            pass
           # task5()
        case _:
            os.system("cls")
            print("\033[96m \033[1m Program was finished \033[00m")
            break


