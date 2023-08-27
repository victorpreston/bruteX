import os
import random

try:
    from colorama import Style, Fore
except ModuleNotFoundError:
    os.system("pip install colorama")

all_colors = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.LIGHTCYAN_EX,
    Style.BRIGHT + Fore.LIGHTBLUE_EX,
    Style.BRIGHT + Fore.LIGHTCYAN_EX,
    Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
    Style.BRIGHT + Fore.LIGHTYELLOW_EX,
]

random_color = random.choice(all_colors)

light_green = Style.BRIGHT + Fore.LIGHTGREEN_EX
green = Style.BRIGHT + Fore.GREEN
light_cyan = Style.BRIGHT + Fore.LIGHTCYAN_EX
cyan = Style.BRIGHT + Fore.CYAN
light_yellow = Style.BRIGHT + Fore.LIGHTYELLOW_EX
yellow = Style.BRIGHT + Fore.YELLOW
red = Style.BRIGHT + Fore.RED
light_red = Style.BRIGHT + Fore.LIGHTRED_EX
