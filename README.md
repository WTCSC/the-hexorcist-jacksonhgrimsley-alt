**HEXORCIST — Universal Base Converter**
HEXORCIST is a lightweight Python utility that converts numbers between arbitrary bases (2–36). It supports both command-line interaction and programmatic use, allowing easy conversion from any supported base to any other.

**Project Structure**
  1.hexorcist/
  2.hexorcist.py = Core logic + CLI interface
  3.test_hexorcist.py = Pytest unit tests
  4.README.md = Project documentation

**Code Overview**
  1.purpose:to_decimal(number_string, original_base)
  
  *requirments*
  1.Converts a string representation of a number from a given base to decimal (base-10).

*Command-Line Mode*
1. When executed directly, the script launches a small interactive prompt:
    --$ python hexorcist.py
Welcome to HEXORCIST, The universal base converter
Enter your number (e.g., C7): C7
Enter the original base (2–36): 16
Enter the target base (2–36): 2

*output*
--C7 (base 16) = 11000111 (base 2)

**Running Tests**
1.This project includes comprehensive pytest unit tests to verify all conversions.
  -Run All Tests
    -pytest test_hexorcist.py
2.Example Test Cases
  -def test_to_decimal_base16():
    assert to_decimal("C7", 16) == 199

**Installation**
1.Clone the repository:
  -git clone
2.nstall pytest for testing:
  -pip install pytest

**License**
  -This project is licensed under the MIT License — feel free to use, modify, and distribute it.

**Contributing**
If you’d like to improve HEXORCIST:
  -Fork the repository
  -Create a new feature branch (git checkout -b feature/awesome-improvement)
  -Commit your changes (git commit -m 'Added awesome improvement')
  -Push to your branch (git push origin feature/awesome-improvement)
  -Open a Pull Request

  
  
