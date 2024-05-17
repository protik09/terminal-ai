#!/usr/bin/env python
import sys
import os
import pathlib
from rich import print
from rich.markdown import Markdown
from groq import Groq
from auth import authGroq, changeApiKey


# Set your GROQ API endpoint URL
GROQ_API_URL = "https://api.groq.io/v1/query"
# Get the absolute path of the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))
# Construct the absolute path for the VERSION file
version_file_path = os.path.join(current_directory, "VERSION")
with open(version_file_path, "r") as f:
    try:
        TERMAI_VERSION = f.read().strip()
        # print(TERMAI_VERSION)
    except ValueError:
        TERMAI_VERSION = "Invalid version number"


def exitHandler(exit_code: int) -> None:
    sys.exit(exit_code)


def main():
    if len(sys.argv) < 2:
        print("Usage: termai <user input>")
        exitHandler(1)

    # user_input = urllib.parse.quote(sys.argv[1])  # Sanitize the user input
    user_input = ""
    for args in sys.argv:
        if args == sys.argv[0]:
            continue
        if args == "-h" or args == "--help":
            print("Usage: termai <user input>")
            exitHandler(0)
        if args == "-v" or args == "--version":
            print(f"{TERMAI_VERSION}")
            exitHandler(0)
        if args == "-c" or args == "--change":
            print("Change the API key for the GROQ API")
            exitHandler(changeApiKey())
        user_input += str(args) + " "
    # print(f"[DEBUG] User input is: {user_input}")

    # Set the query parameters
    client = Groq(api_key=authGroq())
    system_prompt = "You are an AI agent called TermAI. You will reply succinctly to any input you receive. \
        Your replies will be in the Github Markdown format. ALWAYS start your replies with '[TermAI]: ' \
        If providing code snippets, always ensure code highlighting for the appropriate programming language \
        is applied."

    # Send the request to the GROQ API
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        model="llama3-8b-8192",
    )
    reply = chat_completion.choices[0].message.content

    # Print the reply in Markdown using Glow
    print(Markdown(reply))


if __name__ == "__main__":
    main()
