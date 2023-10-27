# test 5th kata example
from kata import five_kata


def test_five_kata():
    result = five_kata.count("abaadjfjcc")
    assert result == {
        'a': 3,
        'b': 1,
        'c': 2,
        'd': 1,
        'f': 1,
        'j': 2,
    }


