#!/usr/bin/env python
from __future__ import annotations
import sys
import os
import argparse
import tiktoken
from rich import print
from rich.markdown import Markdown
from typing import Optional

# from groq import Groq, GroqError
from mygroq import Groq, GroqError
from auth import authGroq, changeApiKey, deleteApiKey

from __init__ import __version__  # noqa: F401
import random
from time import sleep
from ismarkdown import isMarkdown

# Set your GROQ API endpoint URL
GROQ_API_URL: str = "https://api.groq.io/v1/query"

# Models to use
INSTANT_MODEL = "llama-3.3-70b-versatile"
INTERACTIVE_MODEL = "deepseek-r1-distill-llama-70b-specdec"

SYSTEM_PROMPT: str = (
    "You are an AI agent called ProtAI. You will reply succinctly to any input you receive. \
    Your replies will be in the Standard Markdown format. ALWAYS start your replies with '[ProtAI]: ' \
    If providing code snippets, always ensure code highlighting for the appropriate programming language \
    is applied. Always ensure, if sending markdown, that the markdown is sytactically correct. Ensure there \
    are never any single quotes in your reply."
)

NOTE: str = (
    "**Note**: All inputs are 0-shot prompts. There is no multi-turn conversation."
)


def versionHandler() -> None:
    """Print the version number of ProtAI."""
    print(__version__)
    exitHandler(0)

def check_for_updates() -> None:
    """Check if a newer version is available on GitHub."""
    import requests
    try:
        response = requests.get(
            "https://api.github.com/repos/protik09/terminal-ai/tags"
        )
        response.raise_for_status()
        latest_tag = response.json()[0]["name"].lstrip("v")

        if latest_tag > __version__:
            print(
                f"[ProtAI]: Update available! Current: v{__version__}, Latest: v{latest_tag}"
            )
            print("[ProtAI]: Run 'pip install --upgrade protai' to update")
        else:
            print(f"[ProtAI]: Running latest version (v{__version__})")
    except Exception as e:
        print(f"[ProtAI]: Failed to check for updates: {e}")


def exitHandler(exit_code: int) -> None:
    """TODO: Write more comprehensive exit handler when inspiration strikes."""
    sys.exit(exit_code)


# def chatCompletionHandler(
#     client: Groq, system_prompt: str, user_input: str
# ) -> str | None:
#     """Handle the chat completion request."""
#     # Send the request to the GROQ API
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": user_input},
#         ],
#         model=INSTANT_MODEL,
#     )
#     reply: str | None = chat_completion.choices[0].message.content
#     return reply


def checkForUpdate() -> None:
    """Check if the current version is the latest."""
    import requests

    repo_owner = "protik09"
    repo_name = "terminal-ai"
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/tags"
    try:
        response = requests.get(url)
        response.raise_for_status()
        tags = response.json()
        if tags:
            latest_version = tags[0]["name"]
            if latest_version != __version__:
                print(
                    f"{os.linesep}[ProtAI]: A new version ({latest_version}) is available. You are using version {__version__}.{os.linesep}"
                )
            else:
                print(
                    f"{os.linesep}[ProtAI]: You are using the latest version ({__version__}).{os.linesep}"
                )
        else:
            print(
                f"{os.linesep}[ProtAI]: Could not determine the latest version.{os.linesep}"
            )
    except requests.RequestException as e:
        print(f"{os.linesep}[ProtAI]: Failed to check for updates: {e}{os.linesep}")


def chatCompletionHandler(
    client: Groq, system_prompt: str, user_input: str, model: str = INSTANT_MODEL
) -> str | None:
    """Handle the chat completion request."""
    # Send the request to the GROQ API
    chat_completion = client.chat(system_prompt, user_input, model)
    reply: str | None = chat_completion
    return reply


def printReply(reply: str | None) -> None:
    """If the text returned is not markdown, print it as plain text. \
        Otherwise print(Markdown(reply)) doesn't tend to print anything"""
    if isMarkdown(reply):
        print(os.linesep)
        print(
            Markdown(
                reply,
                code_theme="monokai",
            ),
        )
        print(os.linesep)
    else:
        print(f"{os.linesep}{reply}{os.linesep}")


def numTokens(text: str, model: str = "cl100k_base") -> int:
    """Returns the number of tokens in a given text."""
    # Initialize the tokenizer and model
    enc = tiktoken.get_encoding(model)

    return len(enc.encode(text))


def printTokens(input_str: str, reply_str: str) -> None:
    input_tokens = numTokens(input_str)
    output_tokens = numTokens(reply_str)

    print(
        f"{os.linesep}Input tokens ~ {input_tokens} tokens{os.linesep}\
Output tokens ~ {output_tokens} tokens{os.linesep}"
    )


def argParser() -> tuple[Optional[str], argparse.Namespace]:
    parser = argparse.ArgumentParser(description="protai")
    parser.add_argument("user_input", nargs="*", help="User input")
    parser.add_argument("-v", "--version", action="store_true", help="Show the version")
    parser.add_argument(
        "-c",
        "--change",
        action="store_true",
        help="Change the API key for the GROQ API",
    )
    parser.add_argument(
        "-i", "--interactive", action="store_true", help="Interactive mode"
    )
    parser.add_argument(
        "-d", "--delete", action="store_true", help="Delete the current API key"
    )
    args = parser.parse_args()
    _user_input: Optional[str] = None

    if not args.version and not args.change and len(sys.argv) < 2:
        print(f"{os.linesep}Usage: protai <user input> -> For Single line input")
        print(f"Usage: protai -i -> For Interactive mode{os.linesep}")
        exitHandler(0)
    elif args.version:
        versionHandler()
    elif args.delete:
        deleteApiKey()
    elif args.change:
        print("{os.linesep}Change the API key for the GROQ API.{os.linesep}")
        exitHandler(changeApiKey())
    else:
        _user_input = " ".join(args.user_input)
        # print(f"[DEBUG] User input is: {user_input}")
    return (_user_input, args)


def main():
    user_input, args = argParser()
    # Main business logic
    # Set the query parameters
    try:
        client = Groq(api_key=authGroq())
    except GroqError:  # Catch any errors from the Groq class
        print("An error occurred when authenticating with the GROQ API.")

    try:
        if args.interactive:
            print(os.linesep)
            print(Markdown(NOTE))
            print(os.linesep)
            while True:
                user_input = input(">> ").strip()
                # Special tokens for user input
                match user_input.lower():
                    case "exit":
                        raise KeyboardInterrupt
                    case "clear":
                        os.system("cls" if os.name == "nt" else "clear")
                    case "cls":
                        os.system(
                            "cls" if os.name == "nt" else "clear"
                        )  # Yeah yeah I know DRY!!
                        user_input = "clear"
                    case _:
                        pass
                # Send everything else to the chat completion
                reply: str | None = chatCompletionHandler(
                    client, SYSTEM_PROMPT, user_input, model=INTERACTIVE_MODEL
                )
                printReply(reply)
                # printTokens(user_input, reply)
        else:
            reply: str | None = chatCompletionHandler(client, SYSTEM_PROMPT, user_input)
            printReply(reply)
            printTokens(user_input, reply)

    except KeyboardInterrupt:
        # Easter-egg prevent exiting for a few seconds
        if random.randint(0, 100) < 10:  # 10% chance of a random message
            print(
                "{}[HAL 9000]: I'm sorry Dave, I'm afraid I can't do that.{}".format(
                    os.linesep * 2, os.linesep
                )
            )
            sleep(2.6)
            print(
                "{}[ProtAI]: Just Kidding..... Exiting.{}".format(
                    os.linesep, os.linesep
                )
            )
            exitHandler(0)
        else:
            print("{}[ProtAI]: Exiting.....{}".format(os.linesep * 2, os.linesep))
            exitHandler(0)
    except Exception as e:
        print(f"{os.linesep}An error occurred: {e}{os.linesep}")
        exitHandler(1)


if __name__ == "__main__":
    from time import time_ns

    start_time = time_ns()
    main()
    end_time = time_ns()
    print(
        f"{os.linesep * 2}GROQ Time taken: {(end_time - start_time)/1000000:.4f}ms{os.linesep * 2}"
    )
