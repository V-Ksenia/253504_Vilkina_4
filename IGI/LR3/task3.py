from decorator import funcInfoDec

@funcInfoDec
def countSpaces(string):
    """Counts spaces in string"""
    return string.count(" ")

def task3():
    """Runs task3"""
    string = input("Enter string: ")

    print(f"Amount of spaces: {countSpaces(string)}")