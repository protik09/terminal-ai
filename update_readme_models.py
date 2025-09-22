"""
update_readme_models.py
Automatically updates the README.md model references to match those in protai/protai.py.
Run this script before packaging/uploading to PyPI.
"""
import re
import os

PROTAI_PATH = os.path.join("protai", "protai.py")
README_PATH = "README.md"

# Regex patterns to extract model constants
INSTANT_MODEL_RE = re.compile(r'INSTANT_MODEL\s*=\s*["\']([^"\']+)["\']')
INTERACTIVE_MODEL_RE = re.compile(r'INTERACTIVE_MODEL\s*=\s*["\']([^"\']+)["\']')

# Regex patterns to update README model references
README_MODELS_SECTION_RE = re.compile(
    r'(The application uses the following models:[\s\S]*?)(?=### Keeping Model References Up-to-Date)',
    re.MULTILINE
)
PROJECT_DETAILS_MODELS_RE = re.compile(
    r'(## Project Details & Models[\s\S]*?)(?=## Development)',
    re.MULTILINE
)

def extract_models():
    with open(PROTAI_PATH, encoding="utf-8") as f:
        code = f.read()
    instant = INSTANT_MODEL_RE.search(code)
    interactive = INTERACTIVE_MODEL_RE.search(code)
    if not instant or not interactive:
        raise ValueError("Could not find model constants in protai.py")
    return instant.group(1), interactive.group(1)

def update_readme(instant_model, interactive_model):
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    # Update main usage section
    new_models_section = (
        f"The application uses the following models:\n\n"
        f"- **Instant Mode:** `{instant_model}` for fast, zero-shot inference.\n\n"
        f"- **Interactive Mode:** `{interactive_model}` for multi-turn, zero-shot inference.\n\n"
    )
    readme = README_MODELS_SECTION_RE.sub(new_models_section, readme)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"README.md updated with models: Instant='{instant_model}', Interactive='{interactive_model}'")

def main():
    instant, interactive = extract_models()
    update_readme(instant, interactive)

if __name__ == "__main__":
    main()
