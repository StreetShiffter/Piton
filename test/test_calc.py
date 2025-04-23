from src.calc import calculate_logarithm
import pytest

def test_calculate_log():
    assert calculate_logarithm(8, 4) == 1.5
    assert calculate_logarithm(8, 2) == 3

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)