"""
Tests for the mygroq module in protai.

This module provides a Groq class for interacting with the GROQ API. These tests use dummy classes to simulate API responses and avoid real network calls.

Class Descriptions:
-------------------
DummyResponse:
    - Simulates a response object with a status code and JSON data.
DummyGroq:
    - Inherits from mygroq.Groq and overrides the chat method to return a fixed reply, simulating a successful API call.

Test Descriptions:
------------------
1. test_groq_chat:
   - Purpose: Ensure that the DummyGroq's chat method returns a reply that starts with the expected '[ProtAI]:' prefix.
   - How: Instantiates DummyGroq and calls chat with dummy arguments.

Usage:
------
Run these tests with pytest to verify Groq API wrapper logic without making real API requests.
"""
from protai import mygroq

class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data
    def json(self):
        return self._json_data

class DummyGroq(mygroq.Groq):
    def __init__(self, *args, **kwargs):
        super().__init__(api_key="dummy")
        self.headers = {}
    def chat(self, system_prompt, user_prompt, model):
        return "[ProtAI]: Dummy reply"

def test_groq_chat():
    groq = DummyGroq()
    reply = groq.chat("system", "user", "model")
    assert reply.startswith("[ProtAI]:")
