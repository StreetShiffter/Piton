from src.asserts import divide


def test_divide():
    assert divide(2, 1) == 2


def test_zero_divide():
    assert divide(2, 0) == 0
