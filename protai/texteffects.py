
from colorama import Fore, Style


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
    return f"{Fore.GREEN}{success_string}{Style.RESET_ALL}"


def redString(failure_string: str = "") -> str:
    return f"{Fore.RED}{failure_string}{Style.RESET_ALL}"


def yellowString(caution_string: str = "") -> str:
    return f"{Fore.YELLOW}{caution_string}{Style.RESET_ALL}"


def successString(success_string: str = "") -> str:
    return f"{Fore.GREEN}[ ✔ ]  {success_string}{Style.RESET_ALL}"


def errorString(failure_string: str = "") -> str:
    return f"{Fore.RED}[ ✘ ]  {failure_string}{Style.RESET_ALL}"


def warningString(caution_string: str = "") -> str:
    return f"{Fore.YELLOW}[!]  {caution_string}{Style.RESET_ALL}"


if __name__ == "__main__":
    printBanner()
