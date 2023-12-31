import os
import platform
from scripts.colors import random_color, yellow, cyan

try:
    from colorama import Style, Fore
except ModuleNotFoundError:
    os.system("pip install colorama")


def banner():
    """
    Prints the logo and author's info
    """
    logo = f"""
        ...     ..                                       s                                   ..
    .=*8888x <"?88h.                                   :8                         .H88x.  :~)88:
    X>  '8888H> '8888      .u    .      x.    .        .88                        x888888X ~:8888
    '88h. `8888   8888    .d88B :@8c   .@88k  z88u     :888ooo      .u            ~   "8888X  %88"
    '8888 '8888    "88>  ="8888f8888r ~"8888 ^8888   -*8888888   ud8888.               X8888
    `888 '8888.xH888x.    4888>'88"    8888  888R     8888    :888'8888.           .xxX8888xxxd>
    X" :88*~  `*8888>   4888> '      8888  888R     8888    d888 '88%"          :88888888888"
    ~"   !"`      "888>   4888>        8888  888R     8888    8888.+"             ~   '8888
    .H8888h.      ?88   .d888L .+     8888 ,888B .  .8888Lu= 8888L         .    xx.  X8888:    .
    :"^"88888h.    '!    ^"8888*"     "8888Y 8888"   ^%888*   '8888c. .+  .@8c  X888  X88888x.x"
    ^    "88888hx.+"        "Y"        `Y"   'YP       'Y"     "88888%   '%888" X88% : '%8888"
            ^"**""                                                "YP'      ^*    "*=~    `""



                        {cyan + "Author: " + yellow + "Victor Preston | Xpert"}
    """
    print(f"{random_color}{logo}")
    author_info()


def author_info():
    """
    Shows details of the author
    """
    print(random_color + "-" * 63, end="")
    print(
        random_color,
        "\n" + "|" + Style.BRIGHT + Fore.LIGHTCYAN_EX,
        "- " * 4,
        "[+] LinkedIn: Victor Preston ",
        "- " * 11 + random_color + "|",
    )
    print(
        random_color,
        "\n" + "|" + Style.BRIGHT + Fore.LIGHTYELLOW_EX,
        "- " * 4,
        "[+] Twitter: https://twitter.com/vpreston254 ",
        "- " * 3 + random_color + "|",
    )
    print(
        random_color,
        "\n" + "|" + Style.BRIGHT + Fore.LIGHTRED_EX,
        "- " * 4,
        "[+] Github: https://github.com/victorpreston ",
        "- " * 3 + random_color + "|",
    )
    print(random_color + "-" * 63)


def clear():
    """
    Clear the screen based on the OS being used

    Windows uses the 'cls' command, while *nix systems use the 'clear' command
    """
    os.system("cls") if "Windows" in platform.platform() else os.system("clear")
