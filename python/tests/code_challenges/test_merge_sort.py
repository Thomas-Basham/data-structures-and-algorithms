import pytest
from code_challenges.merge_sort import merge_sort


def test_sort():
    lst = [8, 4, 23, 42, 16, 15]
    assert merge_sort(lst) == [4, 8, 15, 16, 23, 42]


def test_negatives():
    lst = [4, -8, 15, -16, 23, -42]
    assert merge_sort(lst) == [-42, -16, -8, 4, 15, 23]


def test_floats():
    lst = [4, 3.8, 15, 2.16, 23, 74.42]
    assert merge_sort(lst) == [2.16, 3.8, 4, 15, 23, 74.42]
