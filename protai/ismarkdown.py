import re

def isMarkdown(text: str) -> bool:
    """Check if a string contains markdown formatting."""
    # Define regex patterns for common markdown elements
    markdown_patterns = [
        r"#{1,6} ",  # Headings (e.g., #, ##, ###, etc.)
        r"\*\*.*\*\*",  # Bold (e.g., **bold**)
        r"\*.*\*",  # Italic (e.g., *italic* or _italic_)
        r"\[.*\]\(.*\)",  # Links (e.g., [text](url))
        r"\!\[.*\]\(.*\)",  # Images (e.g., ![alt](url))
        r"\n\s*[-\*\+] ",  # Unordered list (e.g., - item, * item, + item)
        r"\n\d+\.",  # Ordered list (e.g., 1. item, 2. item)
        r"> ",  # Blockquote (e.g., > quote)
        r"`{1,3}.*`{1,3}",  # Inline code or code block (e.g., `code` or ```code```)
    ]

    # Combine all patterns into a single regex
    combined_pattern = "|".join(markdown_patterns)

    # Search for any markdown pattern in the text
    if re.search(combined_pattern, text):
        return True
    return False

if __name__ == "__main__":

    # Test the function
    text_with_markdown = "This is a **bold** text with [a link](http://example.com)."
    text_without_markdown = "This is a plain text."

    print(isMarkdown(text_with_markdown))  # Output: True
    print(isMarkdown(text_without_markdown))  # Output: False
