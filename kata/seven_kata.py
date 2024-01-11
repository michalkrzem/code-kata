"""
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""


def solution(string: str) -> str:
    """
    Complete the solution so that it reverses the string passed into it.
    param string: text
    :return: reverse string
    """
    try:
        return string[::-1]
    except TypeError:
        return 'Bad typ of value'
