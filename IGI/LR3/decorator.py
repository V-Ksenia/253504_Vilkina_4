
def funcInfoDec(func):
    def wrapper(*args, **kwargs):
        print(f'\033[92m ___Сalling {func.__name__}() '
              f'that {func.__doc__}___ \033[00m')
        result = func(*args, **kwargs)
        return result
    return wrapper


def inputDec(func):
    def wrapper(*args, **kwargs):
        print(f'\033[93m __Expected type: {args.__getitem__(1)} \033[00m')
        result = func(*args, **kwargs)
        return result
    return wrapper