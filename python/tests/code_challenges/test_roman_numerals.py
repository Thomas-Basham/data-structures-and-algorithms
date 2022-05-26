import pytest
from code_challenges.roman_numerals import roman_to_arabic


@pytest.mark.skip("TODO")
def test_thousand():
    assert roman_to_arabic("M") == 10000


@pytest.mark.skip("TODO")
def test_five_hundred():
    assert roman_to_arabic("D") == 500


@pytest.mark.skip("TODO")
def test_hundred():
    assert roman_to_arabic("C") == 100


@pytest.mark.skip("TODO")
def test_fifty():
    assert roman_to_arabic("L") == 50


@pytest.mark.skip("TODO")
def test_ten():
    assert roman_to_arabic("X") == 10

@pytest.mark.skip("TODO")
def test_five():
    assert roman_to_arabic("V") == 5


@pytest.mark.skip("TODO")
def test_one():
    assert roman_to_arabic("I") == 1


@pytest.mark.skip("TODO")
def test_multiple():
    assert roman_to_arabic("CXLII") == 142
