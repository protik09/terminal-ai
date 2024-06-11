#!/usr/bin/env python
from __future__ import annotations
import sys
import argparse
from rich import print
from rich.markdown import Markdown

# from groq import Groq, GroqError
from mygroq import Groq, GroqError
from auth import authGroq, changeApiKey, deleteApiKey

from __init__ import __version__  # noqa: F401
import random
from time import sleep
from ismarkdown import isMarkdown

# Set your GROQ API endpoint URL
GROQ_API_URL = "https://api.groq.io/v1/query"


def versionHandler() -> None:
    """Print the version number of ProtAI."""
    print(__version__)
    exitHandler(0)


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
#         model="llama3-8b-8192",
#     )
#     reply: str | None = chat_completion.choices[0].message.content
#     return reply


def chatCompletionHandler(
    client: Groq, system_prompt: str, user_input: str, model: str = "llama3-8b-8192"
) -> str | None:
    """Handle the chat completion request."""
    # Send the request to the GROQ API
    chat_completion = client.chat(system_prompt, user_input, model)
    reply: str | None = chat_completion
    return reply


def printReply(reply: str | None) -> None:
    """If the text returned is not markdown, print it as plain text. \
        Otherwise print(Mardownm(reply)) doesnt tend to print anything"""
    if isMarkdown(reply):
        print(
            Markdown(
                reply,
                code_theme="monokai",
            ), end="\n"
        )
    else:
        print(f"{reply}\n")


def main():
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

    if not args.version and not args.change and len(sys.argv) < 2:
        print("Usage: protai <user input> -> For Single line input")
        print("Usage: protai -i -> For Interactive mode")
        exitHandler(0)
    elif args.version:
        versionHandler()
    elif args.delete:
        deleteApiKey()
    elif args.change:
        print("\nChange the API key for the GROQ API.\n")
        exitHandler(changeApiKey())
    else:
        user_input = " ".join(args.user_input)
    # print(f"[DEBUG] User input is: {user_input}")

    # Set the query parameters
    try:
        client = Groq(api_key=authGroq())
    except GroqError:  # Catch any errors from the Groq class
        print("An error occurred when authenticating with the GROQ API.")

    system_prompt: str = (
        "You are an AI agent called ProtAI. You will reply succinctly to any input you receive. \
        Your replies will be in the Standard Markdown format. ALWAYS start your replies with '[ProtAI]: ' \
        If providing code snippets, always ensure code highlighting for the appropriate programming language \
        is applied. Always ensure, if sending markdown, that the markdown is sytactically correct. Ensure there \
        are never any single quotes in your reply."
    )

    try:
        if args.interactive:
            note = "\n**Note**: All inputs are 0-shot prompts. There is no multi-turn conversation.\n"
            print(Markdown(note))
            while True:
                user_input = input(">> ").strip()
                if user_input.lower().strip() == "exit":
                    raise KeyboardInterrupt
                reply: str | None = chatCompletionHandler(
                    client, system_prompt, user_input, model="llama3-70b-8192"
                )
                printReply(reply)
        else:
            reply: str | None = chatCompletionHandler(client, system_prompt, user_input)
            printReply(reply)
    except KeyboardInterrupt:
        if random.randint(0, 100) < 10:
            print("\n\n[HAL 9000]: I'm sorry Dave, I'm afraid I can't do that.")
            sleep(2.6)
            print("\n\n[ProtAI]: Just Kidding..... Exiting.\n")
            exitHandler(0)
        else:
            print("\n[ProtAI]: Exiting.....\n")
            exitHandler(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
        exitHandler(1)


if __name__ == "__main__":
    from time import time_ns

    start_time = time_ns()
    main()
    end_time = time_ns()
    print(f"\n\n\nGROQ Time taken: {(end_time - start_time)/1000000:.4f}ms\n\n\n")
