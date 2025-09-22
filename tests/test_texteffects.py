"""
Tests for the texteffects module in protai.

This module provides functions for formatting terminal output with colors and banners.

Test Descriptions:
------------------
1. test_green_string:
    - Purpose: Ensure greenString returns a string containing the input and the ANSI escape code for green text.
    - Example: "success" should be wrapped in green color codes.

2. test_red_string:
    - Purpose: Ensure redString returns a string containing the input and the ANSI escape code for red text.
    - Example: "fail" should be wrapped in red color codes.

3. test_overwrite_prev_line:
    - Purpose: Ensure overwritePrevLine returns a string that starts with the ANSI code to move the cursor up and includes the provided text.
    - Example: "test" should be included after the cursor movement code.

Usage:
------
Run these tests with pytest to verify terminal formatting functions.
"""
from protai import texteffects

def test_green_string():
    result = texteffects.greenString("success")
    assert "success" in result
    # colorama Fore.GREEN is '\x1b[32m' or '\033[32m', but autoreset adds '\033[0m' at end
    assert "[32m" in result

def test_red_string():
    result = texteffects.redString("fail")
    assert "fail" in result
    assert "[31m" in result

def test_overwrite_prev_line():
    text = "test"
    result = texteffects.overwritePrevLine(text)
    assert result.startswith("\033[F")
    assert text in result
