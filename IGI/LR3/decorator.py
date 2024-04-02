
def funcInfoDec(func):
    """Prints name and documentation of a current function"""
    def wrapper(*args, **kwargs):
        print(f'\033[92m ___Сalling {func.__name__}() '
              f'that {func.__doc__}___ \033[00m')
        result = func(*args, **kwargs)
        return result
    return wrapper


def inputDec(func):
    """Prints the type user needs to enter"""
    def wrapper(*args, **kwargs):
        print(f'\033[93m __Expected type: {args.__getitem__(1)} \033[00m')
        result = func(*args, **kwargs)
        return result
    return wrapper