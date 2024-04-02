from enum import Enum
from decorator import inputDec

class TYPES(Enum):
    """Allowed types for input"""
    INT = 1
    FLOAT = 2

@inputDec
def inputValidate(string, type_):
    """Checks user's input"""
    while True:
        match type_:
            case TYPES.INT:
                try:
                    input_ = int(input(f"{string}"))
                    return input_
                except ValueError as err:
                    print(f'\033[91m {str(err)} \033[00m')
            case TYPES.FLOAT:
                try:
                    input_ = float(input(f"{string}"))
                    return input_
                except ValueError as err:
                    print(f'\033[91m {str(err)} \033[00m')
