import pytest

from libs.calculation import addition, substraction


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-2, -3, -5), (0, 0, 0), (10, -5, 5)])
def test_addition(a: int, b: int, expected: int):
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (-2, -3, 1), (0, 0, 0), (10, 15, -5)])
def test_substraction(a: int, b: int, expected: int):
    assert substraction(a, b) == expected
