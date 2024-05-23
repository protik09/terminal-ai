#!/usr/bin/env python
"""
This function handles authentication with the GROQ API

Author: Protik Banerji <protik09@users.noreply.github.com>

"""

import os
import keyring
import re
import keyring.errors
from prompt_toolkit import prompt

KEYRING_SYSTEM: str = "groq"
KEYRING_USER: str = "api-key"
KEYRING_FLAG: bool = False


def _checkKeyringExists() -> bool:
    """Check if keyring exists"""
    keyring_exists: bool = False
    try:
        keyring.get_keyring()  # Check if keyring is available
        keyring_exists = True
    except keyring.errors.NoKeyringError:  # If keyring is not available
        print("[KeyringError]: Keyring is not available. You're probably running in WSL. ProtAI is not aupported in WSL")
        exit(1)
    except keyring.errors.InitError:  # If keyring is not available
        print("[KeyringError]: Keyring initialization failed.")
    except keyring.errors.KeyringLocked:
        print("[KeyringError]: Keyring is locked.")
    return keyring_exists


def _getApiKeyFromKeyring() -> str:
    """Get password from keyring"""
    password: str = None
    if _checkKeyringExists():  # If keyring is available
        try:
            password: str = keyring.get_password(KEYRING_SYSTEM, KEYRING_USER)
        except keyring.errors.KeyringError as e:  # If keyring is not available
            print(f"[KeyringError]: {e}")
    return password


def _getApiKeyUser() -> str:
    """Get API key from user"""
    try:
        api_key = prompt("Enter GROQ API Key: ", is_password=True)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Exiting...")
        exit(1)
    return api_key


def _validateApiKey(api_key: str) -> bool:
    """Validate API key"""
    pattern = re.compile(r"^gsk_[a-zA-Z0-9]{30,1024}$")
    return bool(pattern.match(api_key))


def _deleteApiKey() -> None:
    """Delete API key from keyring and environment variable"""
    if _checkKeyringExists():  # If keyring is available
        try:
            keyring.delete_password(KEYRING_SYSTEM, KEYRING_USER)
            del os.environ["GROQ_API_KEY"]
        except (
            KeyError,
            keyring.errors.PasswordDeleteError,
        ):
            print(
                "[KeyringError]: Failed to delete password in keyring or os.environ. \
                    It's ok though you can still overwrite it."
            )
    else:  # If keyring is not available
        print("[OsEnvError]: GROQ_API_KEY is not available.")


def changeApiKey() -> int:
    """Change API key"""
    error_code = 0
    # Delete key from keyring
    _deleteApiKey()
    # Ask user for password
    api_key = _getApiKeyUser()

    if _validateApiKey(api_key):  # Validate API key
        keyring.set_password(
            KEYRING_SYSTEM, KEYRING_USER, api_key
        )  # Store password in keyring
    else:
        error_code = 1  # Invalid API key

    return error_code


def authGroq() -> str:
    """Get API key either from Environment Variable or Keyring"""
    api_key = None

    # GET API KEY
    # Check if GROQ API Key exists as an environment variable
    if "GROQ_API_KEY" in os.environ:
        api_key = os.environ["GROQ_API_KEY"]
        print("[DEBUG]: GROQ_API_KEY is set as an environment variable")
        if api_key == "":
            print("GROQ_API_KEY is empty")
            del os.environ["GROQ_API_KEY"]  # Delete key from environment
            api_key = None
    elif _getApiKeyFromKeyring() is None:  # If password is not stored in keyring
        # Get password from user
        api_key = _getApiKeyUser()
        # print(f"[DEBUG]: Entered API key length: {len(api_key)}")  # Debugging info
        try:
            # Store password in keyring
            keyring.set_password(KEYRING_SYSTEM, KEYRING_USER, api_key)
        except keyring.errors.PasswordSetError:
            print("[KeyringError]: Failed to set password in keyring")
    else:  # If password is stored in keyring
        api_key = _getApiKeyFromKeyring()  # Get password from keyring

    # Validate API key
    if not _validateApiKey(api_key):
        print("[KeyError]: Invalid API key. Please check your API key.")
        _deleteApiKey()  # Delete API key from keyring and environment variable
        api_key = None
    else:  # It is a valid API Key
        pass
    return api_key


if __name__ == "__main__":
    api_key = authGroq()
    if api_key:
        print("Authentication successful")
    else:
        print("Authentication failed")
