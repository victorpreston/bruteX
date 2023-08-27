import os
import sys
import time
from scripts.colors import cyan


def sprint(str):
    for i in str + cyan + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)


def command(str):
    os.system(str)
