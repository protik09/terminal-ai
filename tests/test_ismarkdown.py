"""
Tests for the ismarkdown module in protai.

This module provides a function to detect whether a string contains Markdown formatting.

Test Descriptions:
------------------
1. test_is_markdown_true:
    - Purpose: Ensure that isMarkdown returns True for strings containing Markdown syntax (e.g., bold, links).
    - Example: "This is a **bold** text with [a link](http://example.com)." should be detected as Markdown.

2. test_is_markdown_false:
    - Purpose: Ensure that isMarkdown returns False for plain text without any Markdown formatting.
    - Example: "This is a plain text." should not be detected as Markdown.

Usage:
------
Run these tests with pytest to verify Markdown detection logic.
"""
from protai import ismarkdown

def test_is_markdown_true():
    text = "This is a **bold** text with [a link](http://example.com)."
    assert ismarkdown.isMarkdown(text) is True

def test_is_markdown_false():
    text = "This is a plain text."
    assert ismarkdown.isMarkdown(text) is False
