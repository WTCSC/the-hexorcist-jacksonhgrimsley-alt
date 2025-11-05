# HEXORCIST — Universal Base Converter

#Purpose:
    #Small command-line utility that converts numbers between bases 2 through 36.
    #It first converts an input string number from an original base to an integer (decimal) and then converts that integer into the requested target base.
#Author: Jackson Grimsley

# Date: 11/5/25

def to_decimal(number_string, original_base):
    #Convert a number string in a given base to its integer (base-10) value.
    #Parameters: number_string (str): The number represented as a string using digits 0-9 and A-Z.
    #Returns: int: The integer (base-10) value of number_string interpreted in original_base.

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0
    power = 0
# move from the least-significant digit (rightmost) to most-significant (leftmost).
    # Reversing the string is a simple way to match each digit to the appropriate power of the base.

    for char in number_string[::-1]:
        # Map characters to numeric value. This will raise ValueError if char is invalid,
        # which preserves the original behavior (no custom error handling introduced).
        char_value = digits.index(char)
        # Accumulate the contribution of this digit according to positional notation:
        # value = digit_value * (base ** position)
        total_value += char_value * (original_base ** power)
        # Move to the next higher power of the base for the next (left) digit.
        power += 1

    return total_value


def from_decimal(decimal_number, target_base):
    # Convert an integer (base-10) into a string representation in the specified target base.

    # Parameters:decimal_number (int): The integer to convert. Expected to be a non-negative.target_base (int): The base to convert to. Expected in the range 2..36.
       #(The function does not explicitly validate the base; unexpected values may lead to incorrect results or errors.)

    #Returns:str: The string representation of decimal_number in target_base using digits 0-9 and A-Z.
             # Example: from_decimal(199, 16) -> "C7"



    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if decimal_number == 0:
        # special case to return to the commonly expected "0" rather than an empty string.
        return "0"
 
 # Repeated division: extract least-significant digit via remainder, then reduce the number.
    # This loop continues until the remaining quotient is zero.
    result_string = ""

    while decimal_number > 0:
        remainder = decimal_number % target_base # next digit (as integer)
        decimal_number //= target_base # integer division reduces the number

# Map remainder to its character form and prepend to result string so digits end up in correct order.
        # Prepending keeps the logic simple and maintains the same external behavior as the original code.

        char_to_add = digits[remainder]
        result_string = char_to_add + result_string

    return result_string


print("Welcome to HEXORCIST, The universal base converter")
 # Program header presented to the user. Kept as interactive CLI per original script.
 
number_string = input("Enter your number (e.g., C7): ")
original_base = int(input("Enter the original base (2–36): "))
target_base = int(input("Enter the target base (2–36): "))
# Read inputs exactly as the original code does (no added validation to preserve behavior).

decimal_value = to_decimal(number_string, original_base)
converted_value = from_decimal(decimal_value, target_base)
# Perform conversions using the helper functions above and print a formatted result.

print(f"\n{number_string} (base {original_base}) = {converted_value} (base {target_base})")

