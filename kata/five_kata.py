#  https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty?
Then the result should be empty object literal, {}.
"""


def count(value):
    # The function code should be here
    try:
        result = {letter: value.count(letter) for letter in set(value)}
    except TypeError:
        return 'Bad typ of parameter in count function'

    return result
