import pytest

from src.revers_list import revert_list


@pytest.mark.parametrize('a, b', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow')
])
def test_reverse(a, b):
    assert revert_list(a) == b
# def test_revert_list_numbers(numbers):
#     assert revert_list('123') == numbers
#     assert revert_list('456') != numbers
#
#
# def test_revert_list_letters(letters):
#     assert revert_list('hello') == letters
