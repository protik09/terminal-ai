#!/usr/bin/env python
"""
This function handles authentication with the GROQ API

Author: Protik Banerji <protik09@users.noreply.github.com>

"""

import os
import keyring
import maskpass
import re


KEYRING_SYSTEM = "groq"
KEYRING_USER = "api-key"


def _getPasswordKeyring() -> str:
    """Get password from keyring"""
    password: str = keyring.get_password(KEYRING_SYSTEM, KEYRING_USER)
    return password


def _validateApiKey(api_key: str) -> bool:
    """Validate API key"""
    pattern = re.compile(r"^gsk_[a-zA-Z0-9]{30,99}$")
    return bool(pattern.match(api_key))


def changeApiKey() -> int:
    """Change API key"""
    error_code = 0
    # Delete key from keyring
    keyring.delete_password(KEYRING_SYSTEM, KEYRING_USER)
    # Ask user for password
    api_key = maskpass.askpass("Enter GROQ API Key: ")  # Mask password

    if _validateApiKey(api_key):  # Validate API key
        keyring.set_password(
            KEYRING_SYSTEM, KEYRING_USER, api_key
        )  # Store password in keyring
    else:
        error_code = 1  # Invalid API key

    return error_code


def authGroq() -> str:
    """Get API key either from Environment Variable or Keyring"""
    # Check if GROQ API Key exists as an environment variable
    if "GROQ_API_KEY" in os.environ:
        api_key = os.environ["GROQ_API_KEY"]
        print("[DEBUG]: GROQ_API_KEY is set as an environment variable")
        if api_key == "":
            print("GROQ_API_KEY is empty")
            del os.environ["GROQ_API_KEY"]  # Delete key from environment
    elif _getPasswordKeyring() is None:  # If password is not stored in keyring
        # Get password from user
        api_key = maskpass.askpass("Enter GROQ API Key: ")  # Mask password
        # Store password in keyring
        keyring.set_password(
            KEYRING_SYSTEM, KEYRING_USER, api_key
        )  # Store password in keyring
    else:  # If password is stored in keyring
        api_key = _getPasswordKeyring()  # Get password from keyring
        # print("[DEBUG]: GROQ_API_KEY is not set as an environment variable")

    # Validate API key
    if not _validateApiKey(api_key):
        print("[KeyError]: Invalid API key. Please check your API key.")
        # Delete key from keyring
        keyring.delete_password(KEYRING_SYSTEM, KEYRING_USER)
        return ""

    return str(api_key)


if __name__ == "__main__":
    pass
