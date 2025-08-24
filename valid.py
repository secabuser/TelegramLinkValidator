import os
import requests
from pystyle import Colors, Colorate, Center
from colorama import Fore, init
from bs4 import BeautifulSoup
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

_g = Fore.GREEN
_r = Fore.RED
_w = Fore.WHITE
_re = Fore.RESET

class _v:
    def __init__(self):
        self._f = "link.txt"
        self._v = "valid.txt"
        self._i = "invalid.txt"
        self._s = 1
        self._m = 5
        self._h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }

    def _c(self):
        os.system("cls" if os.name == "nt" else "clear")

    def _b(self):
        _n = '''
▗▖   ▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▖ ▗▖   ▗▄▄▄▖▗▄▄▄   ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
▐▌     █  ▐▛▚▖▐▌▐▌▗▞▘    ▐▌  ▐▌▐▌ ▐▌▐▌     █  ▐▌  █ ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
▐▌     █  ▐▌ ▝▜▌▐▛▚▖     ▐▌  ▐▌▐▛▀▜▌▐▌     █  ▐▌  █ ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▌ ▐▌     ▝▚▞▘ ▐▌ ▐▌▐▙▄▄▖▗▄█▄▖▐▙▄▄▀ ▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
                                                                                                                                                                                                     
                        t.me/secabuser 
'''
        print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(_n)))

    def _l(self):
        if not os.path.exists(self._f):
            print(f"{_r}[!]{_re} {self._f} not found!")
            exit(1)
        with open(self._f, "r") as _f:
            return [_o.strip() for _o in _f if _o.strip()]

    def _ch(self, _u):
        try:
            _r = requests.get(_u, headers=self._h, timeout=10)
            if _r.status_code != 200:
                return False, None, None, None
            _s = BeautifulSoup(_r.text, "html.parser")

            _t = _s.find("div", class_="tgme_page_title")
            _ti = _t.get_text(strip=True) if _t else "Unknown"

            _me = _s.find(class_="tgme_page_extra")
            if _me:
                _tx = _me.get_text().strip()
                _n = ''.join(filter(str.isdigit, _tx))
                if _n and int(_n) > 0:
                    return True, _ti, int(_n), _u
            return False, None, None, _u
        except Exception:
            return False, None, None, _u

    def _sv(self, _d):
        with open(self._v, "a", encoding="utf-8") as _f:
            for _u, _ti, _m in _d:
                _f.write(f"{_u} | {_ti} | Members: {_m}\n")

    def _si(self, _u):
        with open(self._i, "a", encoding="utf-8") as _f:
            for _u in _u:
                _f.write(_u + "\n")

    def _r(self):
        self._c()
        self._b()

        try:
            self._s = float(input(f"{_w}Sleep > {_re}").strip())
        except:
            self._s = 1

        try:
            self._m = int(input(f"{_w}Max Work > {_re}").strip())
            if self._m < 1:
                self._m = 5
        except:
            self._m = 5

        _li = self._l()
        print(f"{_w}[~] {len(_li)} links : ){_re}")

        _va = []
        _inv = []

        with ThreadPoolExecutor(max_workers=self._m) as _e:
            _fu = {_e.submit(self._ch, _li): _li for _li in _li}
            for _i, _fu in enumerate(as_completed(_fu), 1):
                _is, _t, _me, _u = _fu.result()
                if _is:
                    print(f"{_g}[{_i}/{len(_li)}] Valid: {_u} | {_t} | Members: {_me}{_re}")
                    _va.append((_u, _t, _me))
                else:
                    print(f"{_r}[{_i}/{len(_li)}] Invalid: {_u}{_re}")
                    _inv.append(_u)
                sleep(self._s)

        if _va:
            self._sv(_va)
            print(f"\n{_g}[!]{_re} Saved {len(_va)} valid links to {_w}{self._v}{_re}")
        if _inv:
            self._si(_inv)
            print(f"{_r}[!]{_re} Saved {len(_inv)} invalid links to {_w}{self._i}{_re}")

if __name__ == "__main__":
    _a = _v()
    _a._r()
