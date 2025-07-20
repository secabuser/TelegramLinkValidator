# 💎 Telegram Private Link Generator & Validator

![Tool Screenshot](tool_screenshot.png)

---

## Features

- Generate random private Telegram group/channel links.
- Validate which links are active (based on member count).
- Extract and save valid links along with member count and channel/group name.
- Multi-threaded and fast.

---

## How to Use

### Step 1: Generate Links

1. Run `gen.py` using Python **OR** simply double-click `start.bat` and select `Generate`.
2. Enter the number of random links you'd like to create.
3. All generated links will be saved to `link.txt`.

### Step 2: Validate Links

1. Once you have generated links, run `valid.py` **OR** use `start.bat` and select `Validate`.
2. Input the desired **delay (sleep)** and **max threads** for the validation.
3. The tool will check each link:
   - Valid links will be saved in `valid.txt` along with group/channel name and member count.
   - Invalid links will be saved in `invalid.txt`.

---

## Installation

### Option 1: One-Click Setup (Windows Only)

Simply run the batch file:

```bat
start.bat
```

> This will automatically install all required dependencies and launch the tool.

---

### Option 2: Manual Setup

If you'd prefer to install manually, just run:

```bash
pip install -r req.txt
```

> Make sure you have Python 3.10+ and `pip` installed on your system.

---

My Telegram Channel -> https://www.t.me/secabuser

