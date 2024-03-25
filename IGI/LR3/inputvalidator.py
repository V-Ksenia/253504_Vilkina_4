from enum import Enum

class TYPES(Enum):
    INT = 1
    FLOAT = 2


def inputValidate(string, type_):
    while True:
        match type_:
            case TYPES.INT:
                try:
                    input_ = int(input(f"{string}: "))
                    return input_
                except ValueError as err:
                    print(str(err))
            case TYPES.FLOAT:
                try:
                    input_ = float(input(f"{string}: "))
                    return input_
                except ValueError as err:
                    print(str(err))
