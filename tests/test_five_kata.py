# test 5th kata example
from kata import five_kata


def test_five_kata_with_param():
    result = five_kata.count("abaadjfjcc")
    assert result == {
        'a': 3,
        'b': 1,
        'c': 2,
        'd': 1,
        'f': 1,
        'j': 2,
    }


def test_five_kata_with_empty_param():
    result = five_kata.count("")
    assert result == {}


def test_five_kata_with_number():
    result = five_kata.count(345)
    assert result == 'Bad typ of parameter in count function'