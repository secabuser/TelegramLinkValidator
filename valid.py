import os
import requests
from pystyle import Colors, Colorate, Center
from colorama import Fore, init
from bs4 import BeautifulSoup
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
W = Fore.WHITE
RE = Fore.RESET

class Validator:
    def __init__(self):
        self.f = "link.txt"
        self.valid_file = "valid.txt"
        self.invalid_file = "invalid.txt"
        self.sleep_time = 1
        self.max_workers = 5
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }

    def clr(self):
        os.system("cls" if os.name == "nt" else "clear")

    def bnr(self):
        b = '''



▗▖   ▗▄▄▄▖▗▖  ▗▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▖ ▗▖   ▗▄▄▄▖▗▄▄▄   ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ 
▐▌     █  ▐▛▚▖▐▌▐▌▗▞▘    ▐▌  ▐▌▐▌ ▐▌▐▌     █  ▐▌  █ ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
▐▌     █  ▐▌ ▝▜▌▐▛▚▖     ▐▌  ▐▌▐▛▀▜▌▐▌     █  ▐▌  █ ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
▐▙▄▄▖▗▄█▄▖▐▌  ▐▌▐▌ ▐▌     ▝▚▞▘ ▐▌ ▐▌▐▙▄▄▖▗▄█▄▖▐▙▄▄▀ ▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
                                                                                                                                                                                                     
                        t.me/secabuser 
'''
        print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(b)))

    def load_links(self):
        if not os.path.exists(self.f):
            print(f"{R}[!]{RE} {self.f} not found!")
            exit(1)
        with open(self.f, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def check_link(self, url):
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            if resp.status_code != 200:
                return False, None, None, None
            soup = BeautifulSoup(resp.text, "html.parser")

            
            title_div = soup.find("div", class_="tgme_page_title")
            title = title_div.get_text(strip=True) if title_div else "Unknown"

            member_div = soup.find(class_="tgme_page_extra")
            if member_div:
                text = member_div.get_text().strip()
                number = ''.join(filter(str.isdigit, text))
                if number and int(number) > 0:
                    return True, title, int(number), url
            return False, None, None, url
        except Exception:
            return False, None, None, url

    def save_valid(self, data):
        
        with open(self.valid_file, "a", encoding="utf-8") as f:
            for url, title, members in data:
                f.write(f"{url} | {title} | Members: {members}\n")

    def save_invalid(self, urls):
        with open(self.invalid_file, "a", encoding="utf-8") as f:
            for url in urls:
                f.write(url + "\n")

    def run(self):
        self.clr()
        self.bnr()

        
        try:
            self.sleep_time = float(input(f"{W}Sleep > {RE}").strip())
        except:
            self.sleep_time = 1

        try:
            self.max_workers = int(input(f"{W}Max Work > {RE}").strip())
            if self.max_workers < 1:
                self.max_workers = 5
        except:
            self.max_workers = 5

        links = self.load_links()
        print(f"{W}[~] {len(links)} links : ){RE}")

        valid_links = []
        invalid_links = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.check_link, link): link for link in links}
            for i, future in enumerate(as_completed(futures), 1):
                is_valid, title, members, url = future.result()
                if is_valid:
                    print(f"{G}[{i}/{len(links)}] Valid: {url} | {title} | Members: {members}{RE}")
                    valid_links.append((url, title, members))
                else:
                    print(f"{R}[{i}/{len(links)}] Invalid: {url}{RE}")
                    invalid_links.append(url)
                sleep(self.sleep_time)

        if valid_links:
            self.save_valid(valid_links)
            print(f"\n{G}[!]{RE} Saved {len(valid_links)} valid links to {W}{self.valid_file}{RE}")
        if invalid_links:
            self.save_invalid(invalid_links)
            print(f"{R}[!]{RE} Saved {len(invalid_links)} invalid links to {W}{self.invalid_file}{RE}")

if __name__ == "__main__":
    v = Validator()
    v.run()