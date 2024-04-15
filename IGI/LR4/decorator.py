
def inputDec(func):
    """Prints the type user needs to enter"""
    def wrapper(*args, **kwargs):
        print(f'\033[93m __Expected type: {args.__getitem__(1)} \033[00m')
        result = func(*args, **kwargs)
        return result
    return wrapper