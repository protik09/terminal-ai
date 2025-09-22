# Model Selection & Refresh Logic

## Overview
This document describes the dynamic model selection and daily refresh logic for ProtAI's GROQ integration.

## Features
- **Dynamic Model List**: Models are fetched from the GROQ API and cached locally in `models.json`.
- **Daily Refresh**: The model list is refreshed automatically if the cache is older than 24 hours.
- **Validation & Fallback**: If a requested model is unavailable, ProtAI selects a valid fallback and notifies the user.
- **CLI Integration**: Users can specify a model with `--model` or list available models with `--list-models`.
- **Error Handling**: All model-related errors are reported with clear `[ProtAI]:` messages.

## Usage
- To list available models:
  ```sh
  protai --list-models
  ```
- To specify a model:
  ```sh
  protai --model <model-name> "your query"
  ```
- If a preview model is unavailable, ProtAI will automatically select a valid production model and inform the user.

## Implementation
- See `protai/protai.py` for model selection, validation, and error handling logic.
- See `tests/test_model_selection.py` for tests covering cache refresh, expiry, and fallback behavior.

## Maintenance
- The cache file `models.json` is updated automatically; no manual intervention is required.
- If the GROQ API changes, update the fetch logic in `fetch_groq_models()`.

---
For further details, see the code comments in `protai/protai.py` and the project README.
