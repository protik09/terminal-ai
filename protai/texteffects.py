#!/usr/bin/env python


def checkBgColor() -> None: ...


def pickFontColor() -> None: ...


def printBanner() -> None:
    from platform import machine

    if "arm" in machine():
        pass
    else:
        WELCOME_BANNER = """\n

        ██████╗ ██████╗  ██████╗ ████████╗ █████╗ ██╗
        ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗██║
        ██████╔╝██████╔╝██║   ██║   ██║   ███████║██║
        ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══██║██║
        ██║     ██║  ██║╚██████╔╝   ██║   ██║  ██║██║
        ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝
        \n
        """
        print(WELCOME_BANNER)


def overwritePrevLine(text: str = "") -> str:
    return f"\033[F{text}"


def greenString(success_string: str = "") -> str:
    return f"\x1b[1;32m{success_string}\x1b[0m"


def redString(failure_string: str = "") -> str:
    return f"\x1b[1;31m{failure_string}\x1b[0m"


def yellowString(caution_string: str = "") -> str:
    return f"\x1b[1;33m{caution_string}\x1b[0m"


def successString(success_string: str = "") -> str:
    return f"\x1b[1;32m[ ✔ ]  {success_string}\x1b[0m"


def errorString(failure_string: str = "") -> str:
    return f"\x1b[1;31m[ ✘ ]  {failure_string}\x1b[0m"


def warningString(caution_string: str = "") -> str:
    return f"\x1b[1;33m[!]  {caution_string}\x1b[0m"


if __name__ == "__main__":
    printBanner()
