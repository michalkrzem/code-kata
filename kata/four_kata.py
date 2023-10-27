#  https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def count_calls(func):

    def wrapper(*args, **kwargs):
        if len(str(args[0])) == 1:
            wrapper.counter = 0
            return wrapper.counter
        else:
            wrapper.counter += 1
            func(*args, **kwargs)
            return wrapper.counter

    wrapper.counter = 0

    return wrapper


@count_calls
def multiply(n):
    multiplier = 1
    numbers = [int(number) for number in str(n)]
    for number in numbers:
        multiplier *= number

    if len(str(multiplier)) > 1:
        multiply(multiplier)


def persistence(n):
    counter = multiply(n)
    return counter


print(persistence(4))

