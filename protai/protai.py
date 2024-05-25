#!/usr/bin/env python
import sys
import os
from rich import print
from rich.markdown import Markdown
from groq import Groq, GroqError
from auth import authGroq, changeApiKey
from yaspin import yaspin


# Set your GROQ API endpoint URL
GROQ_API_URL = "https://api.groq.io/v1/query"


def versionHandler() -> None:
    """Print the version number of ProtAI."""
    # Get the absolute path of the current directory
    current_directory = os.path.abspath(os.path.dirname(__file__))
    # Construct the absolute path for the VERSION file
    version_file_path = os.path.join(current_directory, "VERSION")
    with open(version_file_path, "r") as f:
        try:
            ProtAI_VERSION = f.read().strip()
            # print(ProtAI_VERSION)
        except ValueError:
            ProtAI_VERSION = "Invalid version number"
    print(f"{ProtAI_VERSION}")
    exitHandler(0)


def exitHandler(exit_code: int) -> None:
    """TODO: Write more comprehensive exit handler when inspiration strikes."""
    sys.exit(exit_code)


def main():
    if len(sys.argv) < 2:
        print("Usage: protai <user input>")
        exitHandler(1)

    # user_input = urllib.parse.quote(sys.argv[1])  # Sanitize the user input
    user_input = ""
    for args in sys.argv:
        if args == sys.argv[0]:
            continue
        if args == "-h" or args == "--help":
            print("Usage: protai <user input>")
            exitHandler(0)
        if args == "-v" or args == "--version":
            versionHandler()
        if args == "-c" or args == "--change":
            print("Change the API key for the GROQ API")
            exitHandler(changeApiKey())
        user_input += str(args) + " "
    # print(f"[DEBUG] User input is: {user_input}")

    # Set the query parameters
    try:
        client = Groq(api_key=authGroq())
    except GroqError:  # Catch any errors from the Groq class
        print("An error occurred when authenticating with the GROQ API.")

    system_prompt = "You are an AI agent called ProtAI. You will reply succinctly to any input you receive. \
        Your replies will be in the Standard Markdown format. ALWAYS start your replies with '[ProtAI]: ' \
        If providing code snippets, always ensure code highlighting for the appropriate programming language \
        is applied. Always ensure, if sending markdown, that the markdown is sytactically correct."

    with yaspin(text="Processing...", color="green") as spinner:
        try:
            # Send the request to the GROQ API
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ],
                model="llama3-8b-8192",
            )
            reply = chat_completion.choices[0].message.content
            spinner.ok("[✔ ]")  # mark spinner as finished successfully
            # Print the reply in Markdown
            print(Markdown(str("\033[F" + reply)))
        except Exception as e:
            spinner.fail("[✖ ] Processing Failed...")  # mark spinner as failed
            print(f"An error occurred: {e}")
            exitHandler(1)


if __name__ == "__main__":
    main()
