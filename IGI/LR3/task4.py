from inputvalidator import inputValidate, TYPES
from decorator import funcInfoDec


string = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
wordlendict = {}

def dictInit(string: str):
    """Initializes dictionary from given string"""
    for i in string.split(" "):
        if i.__contains__(",") or i.__contains__("."):
            i = i[:len(i) - 1:]
        wordlendict[i] = len(i)
        
    return

@funcInfoDec
def countWordsLessThanFive(string: str):
    """Counts words with lenght less than five"""
    counter = 0

    for i in string.split(" "):
        if i.__contains__(",") or i.__contains__("."):
            i = i[:len(i) - 1:]
        if len(i) < 5:
            counter += 1
    
    return counter

@funcInfoDec
def findShortestDWord():
    """Returns shortest word that ends with letter 'd' """
    dwords = []

    for i in wordlendict:
        if i[len(i) - 1] == 'd':
            dwords.append(i)
    
    return min(dwords)

@funcInfoDec
def printWordsInOrder(string: str):
    """Prints string in reversed order"""
    return sorted(wordlendict, key=wordlendict.get, reverse=True)


def task4():
    """Runs task4"""
    dictInit(string)

    while True:
        choice = inputValidate("Enter function number \n"
                                "1 - Words lenght < 5 \n"
                                "2 - Min word ends with 'd' \n"
                                "3 - Sorted reversed order: ", TYPES.INT)

        match choice:
            case 1:     
                print(f"Words less than 5: {countWordsLessThanFive(string)}")
                return
            case 2:
                print(f"Min word that ends with D: {findShortestDWord()}")
                return
            case 3:
                print(f"Sorted words: {printWordsInOrder(string)}")
                return
            case _:
                print("Incorrect option")
                continue
        