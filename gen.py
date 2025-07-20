import os
import random
import string
from pystyle import Colors, Colorate, Center
from colorama import Fore, init
from time import sleep

init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
W = Fore.WHITE
RE = Fore.RESET

class G:
    def __init__(self):
        self.f = "link.txt"

    def clr(self):
        os.system("cls" if os.name == "nt" else "clear")

    def bnr(self):
        b = '''

▗▖   ▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖     ▗▄▄▖▗▄▄▄▖▗▖  ▗▖
▐▌     █  ▐▛▚▖▐▌▐▌▗▞▘    ▐▌   ▐▌   ▐▛▚▖▐▌
▐▌     █  ▐▌ ▝▜▌▐▛▚▖     ▐▌▝▜▌▐▛▀▀▘▐▌ ▝▜▌
▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▌ ▐▌    ▝▚▄▞▘▐▙▄▄▖▐▌  ▐▌
                                                                  
              t.me/secabuser 
'''
        print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(b)))

    def code(self, l=16):
        c = string.ascii_letters + string.digits
        return ''.join(random.choices(c, k=l))

    def gen(self, n):
        return [f"https://t.me/+{self.code()}" for _ in range(n)]

    def save(self, lst):
        if os.path.exists(self.f):
            os.remove(self.f)
        with open(self.f, "w") as f:
            for i in lst:
                f.write(i + "\n")
        print(f"\n{G}[!]{RE} Saved {len(lst)} links to {W}{self.f}{RE}\n")

if __name__ == "__main__":
    g = G()
    g.clr()
    g.bnr()

    try:
        n = int(input(f"{W}Number > {RE}").strip())
    except:
        print(f"{R}[!]{RE} Invalid number !")
        exit(1)

    g.clr()
    g.bnr()

    print(f"{W}[~] Generating {n} links...{RE}")
    lst = g.gen(n)
    g.save(lst)
    sleep(1)
