import os
import platform
from scripts import colors
c = colors


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
                                                                                               
                                                                                               
                                                                                                                              
                          {c.c + "Author: "+c.y+"Victor Preston | Xpert"}                                                                                                                                   
"""
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")


def banner():
    print(c.ran + logo)
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "[+] LinkedIn: Victor Preston ", "- " * 11+ c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, "[+] Twitter: https://twitter.com/vpreston254 ", "- " * 3+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/victorpreston ", "- " * 3+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, "[+] LinkedIn: Victor Preston ", "- " * 11+ c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, "[+] Twitter: https://twitter.com/vpreston254 ", "- " * 3+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/victorpreston ", "- " * 3+c.ran + "|")

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
