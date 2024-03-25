wordlendict = {}
def dictInit(string: str):
    for i in string.split(" "):
        if i.__contains__(",") or i.__contains__("."):
            i = i[:len(i)-1:]
        wordlendict[i] = len(i)
        
    return


def countWordsLessThanFive(string: str):
    counter = 0

    for i in string.split(" "):
        if i.__contains__(",") or i.__contains__("."):
            i = i[:len(i)-1:]
        if len(i) < 5:
            counter += 1
    
    return counter


def findShortestDWord():
    dwords = []

    for i in wordlendict:
        if i[len(i) - 1] == 'd':
            dwords.append(i)
    
    return min(dwords)


    

def printWordsInOrder(string: str):
    print(f"Sorted words: {sorted(wordlendict, key=wordlendict.get, reverse=True)}")


def task4():
    string = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

    dictInit(string)

    choice = int(input("Enter function number: "))

    match choice:
        case 1:     
            print(f"Words less than 5: {countWordsLessThanFive(string)}")
            return
        case 2:
            print(f"Min word that ends with D: {findShortestDWord()}")
            return
        case 3:
            printWordsInOrder(string)
            return
        