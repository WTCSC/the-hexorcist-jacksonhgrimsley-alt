import pytest
from hexorcist import from_decimal, to_decimal

def test_to_decimal_base16():
    assert to_decimal("C7", 16) == 199
def test_to_decimal_base2():
    assert to_decimal("1101", 2) == 13
def test_to_decimal_base10():
    assert to_decimal("123", 10) == 123
def test_to_decimal_with_letters():
    assert to_decimal("Z", 36) == 35
def test_from_decimal_base16():
    assert from_decimal(199, 16) == "C7"
def test_from_decimal_base2():
    assert from_decimal(13, 2) == "1101"
def test_from_decimal_base36():
    assert from_decimal(35, 36) == "Z"
def test_zero_case():
    assert to_decimal("0", 2) == 0
    assert from_decimal(0, 16) == "0"
