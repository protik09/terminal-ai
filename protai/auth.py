#!/usr/bin/env python
"""
This function handles authentication with the GROQ API

Author: Protik Banerji <protik09@users.noreply.github.com>

"""

import os
import re
import keyring
import keyring.errors

# This dependancy exists solely so I can give user feedback when typing in a masked password
from prompt_toolkit import prompt
from texteffects import printBanner, successString, errorString

KEYRING_SYSTEM: str = "groq"
KEYRING_USER: str = "api-key"
API_KEY_MIN_SIZE: int = 30
API_KEY_MAX_SIZE: int = 1024

def _version() -> None:
    """Check version of ProtAI"""
    from __init__ import __version__
    print(f"\nVersion: {__version__}\n")

def _checkKeyringExists() -> bool:
    """Check if keyring exists"""
    keyring_exists: bool = False
    try:
        keyring.get_keyring()  # Check if keyring is available
        keyring_exists = True
    except keyring.errors.NoKeyringError:  # If keyring is not available
        print(
            "[KeyringError]: Keyring is not available. You're probably running in WSL. \
ProtAI is not aupported in WSL"
        )
        exit(1)
    except keyring.errors.InitError:  # If keyring is not available
        print("[KeyringError]: Keyring initialization failed.")
        exit(1)
    except keyring.errors.KeyringLocked:
        print("[KeyringError]: Keyring is locked.")
        exit(1)
    return keyring_exists


def _getApiKeyFromKeyring() -> str | None:
    """Get password from keyring"""
    password: str | None = None
    if _checkKeyringExists():  # If keyring is available
        try:
            password = keyring.get_password(KEYRING_SYSTEM, KEYRING_USER)
        except keyring.errors.KeyringError as e:  # If keyring is not available
            print(f"[KeyringError]: {e}")
            exit(1)
    return password


def _getApiKeyUser() -> str:
    """Get API key from user"""
    try:
        print("The FREE API key from GROQ can be obtained at [Groq AI website](https://console.groq.com/keys)")
        api_key = prompt("Enter GROQ API Key: ", is_password=True)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Exiting...")
        exit(1)
    return api_key


def _validateApiKey(api_key: str | None) -> bool:
    """Validate API key"""
    if api_key is None:
        return False
    pattern = re.compile(
        r"^gsk_[a-zA-Z0-9]{"
        + str(API_KEY_MIN_SIZE)
        + r","
        + str(API_KEY_MAX_SIZE)
        + r"}$"  # regex "^gsk_[a-zA-Z0-9]{30,1024}$"
    )
    return bool(pattern.match(api_key))


def deleteApiKey() -> None:
    """Delete API key from keyring and environment variable"""
    if _checkKeyringExists():  # If keyring is available
        try:
            keyring.delete_password(KEYRING_SYSTEM, KEYRING_USER)
        except keyring.errors.PasswordDeleteError:
            print(errorString("[KeyringError]: No such password in keyring."))

        try:
            del os.environ["GROQ_API_KEY"]
        except KeyError:
            #             print(
            #                 "[KeyringError]: Failed to delete password in os.environ. \
            # It's ok though you can still overwrite it." )
            pass
        print(successString("API key deleted"))
    else:  # If keyring is not available
        print(errorString("[OsEnvError]: GROQ_API_KEY is not available."))

    exit(0) # TODO: Add error returnj codes.


def changeApiKey() -> int:
    """Change API key"""
    error_code = 0
    # Delete key from keyring
    deleteApiKey()
    # Ask user for password
    api_key = _getApiKeyUser()

    if _validateApiKey(api_key):  # Validate API key
        keyring.set_password(
            KEYRING_SYSTEM, KEYRING_USER, api_key
        )  # Store password in keyring
    else:
        error_code = 1  # Invalid API key

    return error_code


def authGroq() -> str | None:
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
        # Looks like its probably the first time you're running the program
        printBanner()
        _version()
        # Get password from user
        api_key = _getApiKeyUser()
        # print(f"[DEBUG]: Entered API key length: {len(api_key)}")  # Debugging info
        try:
            # Store password in keyring
            keyring.set_password(KEYRING_SYSTEM, KEYRING_USER, api_key)
        except keyring.errors.PasswordSetError:
            print("[KeyringError]: Failed to set password in keyring")
    else:  # If password is stored in keyring
        api_key = _getApiKeyFromKeyring()

    # Validate API key
    if not _validateApiKey(api_key):
        print("[KeyError]: Invalid API key. Please check your API key.")
        deleteApiKey()
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
