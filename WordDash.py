#!/usr/bin/env python3
import itertools
import random
import sys
from datetime import datetime

# =======================
# Banner
# =======================

def banner():

    print("""
          

                                        d8b                   d8b      
                                        88P                    ?88      
                                       d88                      88b     
   ?88   d8P  d8P d8888b   88bd88b d888888   d888b8b   .d888b,  888888b 
   d88  d8P' d8P'd8P' ?88  88P'  `d8P' ?88  d8P' ?88   ?8b,     88P `?8b
   ?8b ,88b ,88' 88b  d88 d88     88b  ,88b 88b  ,88b    `?8b  d88   88P
   `?888P'888P'  `?8888P'd88'     `?88P'`88b`?88P'`88b`?888P' d88'   88b
                                                                                          
                                                                      
                                               Custom Wordlist Generator
                                                           ~CoderKitty🛡️
           """)


# =======================
# Menu
# =======================
def menu():
    print("""
[1] Wordlist based on basic info
[2] Wordlist based on email / username
[3] Wordlist for web application / login
[4] Wordlist for OTP
[5] Common wordlist links
[0] Exit
    """)

# =======================
# Utilities
# =======================
def save_wordlist(filename, data):
    data = sorted(set(data))
    random.shuffle(data)
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(item + "\n")
    print(f"[+] Wordlist saved as: {filename} ({len(data)} entries)")

def leet_transform(word):
    table = {
        "a": ["a", "@", "4"],
        "e": ["e", "3"],
        "i": ["i", "1"],
        "o": ["o", "0"],
        "s": ["s", "$", "5"],
        "t": ["t", "7"]
    }
    results = set([""])
    for char in word.lower():
        new = set()
        for r in results:
            if char in table:
                for rep in table[char]:
                    new.add(r + rep)
            else:
                new.add(r + char)
        results = new
    return results

# =======================
# 1) Basic Info Wordlist
# =======================
def basic_info():
    name = input("First Name: ").strip().lower()
    lname = input("Last Name (optional): ").strip().lower()
    nickname = input("Nickname (optional): ").strip().lower()

    fname = input("Father Name (optional): ").strip().lower()
    fdob = input("Father DOB (DD-MM-YYYY, optional): ").strip()

    mname = input("Mother Name (optional): ").strip().lower()
    mdob = input("Mother DOB (DD-MM-YYYY, optional): ").strip()

    dob = input("Target DOB (DD-MM-YYYY): ").strip()
    fav_num = input("Favorite number (optional): ").strip()

    # ----------------------------
    # DOB Parsing Helper
    # ----------------------------
    def parse_dob(dob):
        try:
            d, m, y = dob.split("-")
            return d, m, y, y[-2:]
        except:
            return None

    user_dob = parse_dob(dob)
    if not user_dob:
        print("Invalid DOB format!")
        return

    dob_values = [user_dob]

    if fdob:
        parsed = parse_dob(fdob)
        if parsed:
            dob_values.append(parsed)

    if mdob:
        parsed = parse_dob(mdob)
        if parsed:
            dob_values.append(parsed)

    # ----------------------------
    # Base Words Collection
    # ----------------------------
    base_words = {name}
    if lname: base_words.add(lname)
    if nickname: base_words.add(nickname)
    if fname: base_words.add(fname)
    if mname: base_words.add(mname)

    base_words.add(name + lname)

    # ----------------------------
    # Extended Symbols
    # ----------------------------
    symbols = ["", "@", "_", ".", "!", "*", "#", "$", "%", "&", "^"]

    wordlist = set()

    # ----------------------------
    # Wordlist Generation
    # ----------------------------
    for word in base_words:
        if not word:
            continue

        wordlist.add(word)
        wordlist.add(word.capitalize())

        for leet in leet_transform(word):
            for sym in symbols:
                for d, m, y, yy in dob_values:
                    wordlist.update({
                        f"{leet}{sym}{d}{m}",
                        f"{leet}{sym}{y}",
                        f"{leet}{sym}{yy}",
                        f"{leet}{sym}{d}{m}{yy}",
                        f"{leet.capitalize()}{sym}{yy}"
                    })

                if fav_num:
                    wordlist.add(f"{leet}{sym}{fav_num}")

    save_wordlist("basic_info_wordlist.txt", wordlist)

# =======================
# 2) Email / Username
# =======================
def email_username():
    # ----------------------------
    # Inputs
    # ----------------------------
    fname = input("First Name: ").strip().lower()
    lname = input("Last Name (optional): ").strip().lower()
    dob = input("Target DOB (DD-MM-YYYY): ").strip()

    username = input("Username (optional): ").strip().lower()
    email = input("Email (optional): ").strip().lower()

    if not fname:
        print("First name is mandatory!")
        return

    if not username and not email:
        print("Either username or email must be provided!")
        return

    # ----------------------------
    # DOB Parsing
    # ----------------------------
    d = m = y = yy = ""
    if dob:
        try:
            d, m, y = dob.split("-")
            yy = y[-2:]
        except:
            print("Invalid DOB format! Use DD-MM-YYYY")
            return

    # ----------------------------
    # Email Parts
    # ----------------------------
    email_user = ""
    email_domain = ""
    if email and "@" in email:
        email_user, email_domain = email.split("@", 1)

    # ----------------------------
    # Name Variations
    # ----------------------------
    names = {fname}
    if lname:
        names.update({
            lname,
            fname + lname,
            fname[0] + lname,
            lname + fname
        })

    # ----------------------------
    # Base Words
    # ----------------------------
    bases = set(names)
    if username:
        bases.add(username)
    if email_user:
        bases.add(email_user)

    # ----------------------------
    # Separators
    # ----------------------------
    separators = ["", ".", "_", "-", "__", ".."]

    wordlist = set()

    # ----------------------------
    # Username Generation
    # ----------------------------
    for base in bases:
        for name in names:
            for sep in separators:
                wordlist.add(f"{base}{sep}{name}")
                wordlist.add(f"{name}{sep}{base}")

                if dob:
                    wordlist.update({
                        f"{base}{sep}{y}",
                        f"{base}{sep}{yy}",
                        f"{name}{sep}{y}",
                        f"{name}{sep}{yy}",
                        f"{base}{sep}{d}{m}",
                        f"{name}{sep}{d}{m}",
                        f"{base}{sep}{name}{sep}{yy}"
                    })

    # ----------------------------
    # Email Generation
    # ----------------------------
    if email_domain:
        for word in list(wordlist):
            wordlist.add(f"{word}@{email_domain}")

    # ----------------------------
    # Add Originals
    # ----------------------------
    if username:
        wordlist.add(username)
    if email:
        wordlist.add(email)

    save_wordlist("username_wordlist.txt", wordlist)

# =======================
# 3) Web App Login
# =======================
def web_login():
    name = input("Name: ").strip().lower()
    dob = input("DOB (DD-MM-YYYY): ").strip()
    app = input("App / Company name: ").strip().lower()
    keywords = input("Keywords (comma separated): ").split(",")

    try:
        d, m, y = dob.split("-")
        yy = y[-2:]
    except:
        print("Invalid DOB format!")
        return

    symbols = ["@", "!", "_", "#", ""]
    usernames = set()
    passwords = set()

    base = {name, app}
    base.update(k.strip().lower() for k in keywords if k.strip())

    for b in base:
        usernames.add(b)
        usernames.add(f"{b}{yy}")
        usernames.add(f"{b}_{app}")

        for leet in leet_transform(b):
            for sym in symbols:
                passwords.update({
                    f"{leet}{sym}123",
                    f"{leet}{sym}{d}{m}",
                    f"{leet}{sym}{yy}",
                    f"{leet.capitalize()}{sym}{app}"
                })

    save_wordlist("web_usernames.txt", usernames)
    save_wordlist("web_passwords.txt", passwords)

# =======================
# 4) OTP Wordlist
# =======================
def otp_wordlist():
    length = int(input("OTP length (4/6/8): "))
    if length < 1 or length > 8:
        print("Invalid OTP length")
        return

    filename = f"otp_{length}_digit.txt"
    count = 0

    with open(filename, "w") as f:
        for otp in itertools.product("0123456789", repeat=length):
            f.write("".join(otp) + "\n")
            count += 1

    print(f"[+] OTP wordlist generated: {filename} ({count} entries)")

# =======================
# 5) Common Wordlist Links
# =======================
def common_links():
    print("""
Common Wordlist Resources:

- SecLists:
  https://github.com/danielmiessler/SecLists

- RockYou:
  https://github.com/brannondorsey/naive-hashcat/releases

- CrackStation:
  https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm

- Probable Wordlists:
  https://github.com/berzerk0/Probable-Wordlists
    """)

# =======================
# Main Loop
# =======================
def main():
    banner()
    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            basic_info()
        elif choice == "2":
            email_username()
        elif choice == "3":
            web_login()
        elif choice == "4":
            otp_wordlist()
        elif choice == "5":
            common_links()
        elif choice == "0":
            print("Exiting WordDash. Stay ethical 🛡️")
            sys.exit()
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
