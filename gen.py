import os
import random
import string
from pystyle import Colors, Colorate, Center
from colorama import Fore, init
from time import sleep

init(autoreset=True)

_g = Fore.GREEN
_r = Fore.RED
_w = Fore.WHITE
_re = Fore.RESET

class _g_class:
    def __init__(self):
        self._f = "link.txt"

    def _c(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _b(self):
        _n = '''

▗▖   ▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖     ▗▄▄▖▗▄▄▄▖▗▖  ▗▖
▐▌     █  ▐▛▚▖▐▌▐▌▗▞▘    ▐▌   ▐▌   ▐▛▚▖▐▌
▐▌     █  ▐▌ ▝▜▌▐▛▚▖     ▐▌▝▜▌▐▛▀▀▘▐▌ ▝▜▌
▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▌ ▐▌    ▝▚▄▞▘▐▙▄▄▖▐▌  ▐▌
                                                                  
              t.me/secabuser 
'''
        print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(_n)))

    def _co(self, _l=16):
        _c = string.ascii_letters + string.digits
        return ''.join(random.choices(_c, k=_l))

    def _ge(self, _n):
        return [f"https://t.me/+{self._co()}" for _ in range(_n)]

    def _s(self, _l):
        if os.path.exists(self._f):
            os.remove(self._f)
        with open(self._f, "w") as _f:
            for _i in _l:
                _f.write(_i + "\n")
        print(f"\n{_g}[!]{_re} Saved {len(_l)} links to {_w}{self._f}{_re}\n")

if __name__ == "__main__":
    _a = _g_class()
    _a._c()
    _a._b()

    try:
        _n = int(input(f"{_w}Number > {_re}").strip())
    except:
        print(f"{_r}[!]{_re} Invalid number !")
        exit(1)

    _a._c()
    _a._b()

    print(f"{_w}[~] Generating {_n} links...{_re}")
    _l = _a._ge(_n)
    _a._s(_l)
    sleep(1)
