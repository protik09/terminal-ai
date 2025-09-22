"""
Tests for the authentication module in protai.

These tests use pytest's monkeypatch fixture to mock keyring and authentication behaviors.

What is monkeypatch?
--------------------
Pytest's monkeypatch fixture allows you to temporarily change ("patch") attributes, methods, or environment variables during a test. This is useful for isolating tests from external dependencies or for simulating specific conditions. For example, you can replace a function with a dummy implementation, or mock a system call.

Test Descriptions:
------------------
1. test_check_keyring_exists:
    - Purpose: Verify that _checkKeyringExists returns True when keyring is available.
    - How: monkeypatches keyring.get_keyring to always succeed, simulating a working keyring backend.

2. test_get_api_key_from_keyring:
    - Purpose: Verify that _getApiKeyFromKeyring retrieves the API key from keyring correctly.
    - How: monkeypatches _checkKeyringExists to always return True, and keyring.get_password to return a dummy key.

Usage:
------
Run these tests with pytest. The monkeypatch fixture is automatically injected by pytest when you declare it as a function argument.
"""
from protai import auth

def test_check_keyring_exists(monkeypatch):
    monkeypatch.setattr(auth.keyring, "get_keyring", lambda: True)
    assert auth._checkKeyringExists() is True

def test_get_api_key_from_keyring(monkeypatch):
    monkeypatch.setattr(auth, "_checkKeyringExists", lambda: True)
    monkeypatch.setattr(auth.keyring, "get_password", lambda system, user: "dummy-key")
    assert auth._getApiKeyFromKeyring() == "dummy-key"
