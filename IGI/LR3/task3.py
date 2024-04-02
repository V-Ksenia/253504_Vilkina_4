from decorator import funcInfoDec

@funcInfoDec
def countSpaces(string):
    """Counts spaces in string"""
    return string.count(" ")

def task3():
    """Runs task3 \n
    Task: Count the number of spaces in the entered string
    """
    string = input("Enter string: ")

    print(f"Amount of spaces: {countSpaces(string)}")