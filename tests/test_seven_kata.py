import pytest
from kata import seven_kata


@pytest.mark.parametrize(
    'text_input,expected',
    [
        ('mama', 'amam'),
        ('tata', 'atat'),
        ('mam zawsze racje', 'ejcar ezswaz mam'),
        ('kot', 'tok'),
    ]
)
def test_solution_with_text(text_input, expected):
    seven_kata_result = seven_kata.solution(text_input)

    assert seven_kata_result == expected


@pytest.mark.parametrize(
    'text_input,expected',
    [
        (5, 'Bad typ of value'),
        ({}, 'Bad typ of value'),
        (True, 'Bad typ of value'),
    ]
)
def test_solution_type_error_value(text_input, expected):
    seven_kata_result = seven_kata.solution(text_input)

    assert seven_kata_result == expected
