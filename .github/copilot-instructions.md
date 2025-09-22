# Copilot Instructions for terminal-ai

## Project Overview
- **terminal-ai** is a zero-shot AI assistant CLI tool for the terminal, powered by the GROQ AI API.
- The main entry point is `protai/protai.py`, which parses CLI arguments, manages authentication, and interacts with the GROQ API via `mygroq.py`.
- The project supports both instant and interactive modes, using different models for each (`llama-3.3-70b-versatile` and `openai/gpt-oss-120b`).
- API keys are securely managed using the `keyring` library and can be changed or deleted via CLI flags.

## Key Components
- `protai/protai.py`: CLI entry, argument parsing, main logic, reply formatting, and error handling.
- `protai/auth.py`: Handles API key storage, retrieval, validation, and user prompts (uses `prompt-toolkit` for masked input).
- `protai/mygroq.py`: Custom wrapper for GROQ API requests (uses `requests` and `orjson`).
- `protai/texteffects.py`: Terminal output formatting (success, error, warning, banners).
- `protai/ismarkdown.py`: Detects markdown formatting in replies for proper rendering.
- `protai/__init__.py` and `VERSION`: Version management, used for update checks and CLI version reporting.

## Developer Workflows
- **Setup**: Use `activate_venv.sh` (Linux/macOS) or `activate_venv.ps1` (Windows) to create and activate a virtual environment.
- **Install dependencies**: `pip install -r requirements.txt`
- **Run CLI**: `python -m protai.protai <query>` or use the installed `protai` command.
- **Change API Key**: `protai --change`
- **Delete API Key**: `protai --delete`
- **Interactive Mode**: `protai -i` (type `exit` or `clear` to leave/clear)
- **Build/Publish**: Use `python setup.py upload` (requires `twine`).

## Patterns & Conventions
- All user-facing replies start with `[ProtAI]: ` and are formatted in Markdown when possible.
- API keys are never stored in plaintext; always use `keyring`.
- Error and exit messages use colored formatting from `texteffects.py`.
- The CLI is strictly zero-shot; no multi-turn conversation is supported.
- WSL2 is not supported due to keyring issues.
- Only the maintainer can publish to PyPI; contributors should fork and submit PRs.

## Integration Points
- **GROQ API**: All AI interactions are routed through `mygroq.py` using the provided API key.
- **Rich library**: Used for Markdown rendering in the terminal.
- **Token counting**: Uses `tiktoken` to display input/output token counts.

## Example: Adding a New Model
- Update model constants in `protai/protai.py` and ensure the model name is passed to `mygroq.py`.
- Test with both instant and interactive modes to verify correct routing.

## References
- See `README.md` for installation, usage, and contribution guidelines.
- See `setup.py` for packaging and publishing details.
- See `protai/protai.py` for CLI argument patterns and main logic.

---

If any section is unclear or missing, please provide feedback so this guide can be improved for future AI agents.
