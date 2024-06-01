#!/usr/bin/env python

from __future__ import annotations, print_function
import requests
import orjson as json


class GroqError(Exception):
    pass


class Groq:
    def __init__(
        self,
        api_key: str | None = None,
        query: str | None = None,
        url: str = "https://api.groq.com/openai/v1/chat/completions",
    ):
        self.query = query
        self.url = url
        self.api_key = api_key
        if api_key:
            self.headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        else:
            raise GroqError()

    def chat(
        self,
        system_prompt: str = "You are a helpful assistant.",
        user_prompt: str = "Reply with - Please write user prompt",
        model: str = "llama3-8b-8192",
    ) -> str:
        """Send a chat message to the GROQ API."""
        _ = model
        data = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "model": model,
        }
        response = requests.post(
            self.url,
            headers=self.headers,
            json=data,
        )
        if response.status_code == 200:
            # Parse the response data
            data_json = response.json()
            data = json.loads(
                json.dumps(data_json).decode("utf-8")
            )  # To ensure correct quotes in json
            return data["choices"][0]["message"]["content"]
        else:
            raise GroqError(response.text)
