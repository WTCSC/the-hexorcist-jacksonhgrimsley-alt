# File name: HEXORCIST

# Author: Jackson Grimsley

# Date 11/5/25

# Description: This module contains unit tests for the `hexorcist` module, specifically      the `to_decimal` and `from_decimal` functions. These tests validate      conversions between decimal and various numeral systems 

# Purpose:The purpose of this file is to verify that number base conversions     performed by `hexorcist` are accurate, handle edge cases correctly,     and maintain consistent behavior across supported bases.





import pytest

from hexorcist import from_decimal, to_decimal

def test_to_decimal_base16():

    #Functionality: Ensures that the `to_decimal` function correctly interprets a hexadecimal string ('C7') as a decimal value (199). This verifies correct handling of alphabetic digits and base-16 computation logic.
    assert to_decimal("C7", 16) == 199
def test_to_decimal_base2():

    #Functionality: Confirms that `to_decimal`accurately converts the binary string '1101' to decimal 13.This validates bitwise positional weighting in base-2 conversions.
    assert to_decimal("1101", 2) == 13
def test_to_decimal_base10():

    #Functionality: Ensures that a numeric string in base-10 ('123') remains unchanged when converted, confirming that the function correctly handles the simplest case where input base equals the target base.
    assert to_decimal("123", 10) == 123
def test_to_decimal_with_letters():

    #Functionality:Verifies that `to_decimal` interprets alphabetic characters as valid digits in higher bases (base-36). For example, 'Z' represents 35 in base-36, confirming proper character-index mapping.
    assert to_decimal("Z", 36) == 35
def test_from_decimal_base16():

    # Functionality: Ensures `from_decimal` correctly converts 199 to 'C7' in base-16.This validates that both uppercase letter output and digit weightingin hexadecimal conversion are correctly implemented.
    assert from_decimal(199, 16) == "C7"
def test_from_decimal_base2():

    #Functionality:Confirms that `from_decimal` properly transforms decimal 13 into binary '1101', verifying that bit representation and order are computed correctly.
    assert from_decimal(13, 2) == "1101"
def test_from_decimal_base36():

    #Functionality:Validates that `from_decimal` maps decimal 35 to 'Z' when using base-36. This confirms correct handling of digit values above 9 (A–Z mapping).
    assert from_decimal(35, 36) == "Z"
def test_zero_case():

    #Functionality:Ensures that both `to_decimal` and `from_decimal` handle zero correctly regardless of the base. Zero is a universal constant across all bases and should consistently map to '0' or 0.
    assert to_decimal("0", 2) == 0
    assert from_decimal(0, 16) == "0"
