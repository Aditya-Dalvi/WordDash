# 🧠 WordDash – Custom Wordlist Generator

WordDash is an **open‑source, interactive wordlist generator** designed for **ethical hacking, penetration testing, CTFs, and security research**. It creates highly customized wordlists based on user‑provided information such as names, DOBs, usernames, emails, applications, and OTP patterns.

> ⚠️ **Disclaimer**: This tool is intended **only for educational purposes and authorized security testing**. Do **NOT** use it on systems you do not own or have explicit permission to test.

---

## ✨ Features

* 🎯 **Target‑based wordlists** using personal & contextual information
* 🔐 **Username & email pattern generation**
* 🌐 **Web application login wordlists** (usernames + passwords)
* 🔢 **OTP brute‑force wordlist generator** (4/6/8 digits)
* 🧬 **Leetspeak transformations** (`a → @ / 4`, `e → 3`, etc.)
* 🎲 **Randomized & de‑duplicated output**
* 📚 Quick access to **popular public wordlists** (SecLists, RockYou)

---

## 🗂 Menu Options Overview

| Option | Description                                      |
| ------ | ------------------------------------------------ |
| 1      | Wordlist based on **basic personal information** |
| 2      | Wordlist based on **email / username patterns**  |
| 3      | Wordlist for **web application login**           |
| 4      | **OTP numeric wordlists** (brute‑force)          |
| 5      | Links to **common public wordlists**             |
| 0      | Exit                                             |

---

## 🛠 Requirements

* Python **3.7+**
* Linux / macOS / Windows
* No external dependencies (pure Python)

---

## 📥 Installation / Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/worddash.git
cd worddash
```

### 2️⃣ Make Script Executable (Linux/macOS)

```bash
chmod +x worddash.py
```

### 3️⃣ Run the Tool

```bash
./worddash.py
# OR
python3 worddash.py
```

---

## 🚀 Usage Guide

When you run WordDash, you’ll see a banner and menu:

```text
[1] Wordlist based on basic info
[2] Wordlist based on email / username
[3] Wordlist for web application / login
[4] Wordlist for OTP
[5] Common wordlist links
[0] Exit
```

### 🔹 Option 1: Basic Info Wordlist

Generates passwords using:

* First / last / nickname
* Parents’ names & DOBs
* Target DOB
* Favorite numbers
* Leetspeak + symbols

📄 Output:

```
basic_info_wordlist.txt
```

---

### 🔹 Option 2: Email / Username Wordlist

Generates:

* Username permutations
* Email‑style usernames
* DOB‑based patterns

📄 Output:

```
username_wordlist.txt
```

---

### 🔹 Option 3: Web Application Login

Generates:

* Likely usernames
* Common password patterns
* App / company‑based passwords

📄 Outputs:

```
web_usernames.txt
web_passwords.txt
```

---

### 🔹 Option 4: OTP Wordlist

Generates **all numeric combinations** for a given OTP length.

Supported lengths:

* 4 digits (10,000 entries)
* 6 digits (1,000,000 entries)
* 8 digits (⚠️ very large)

📄 Output:

```
otp_4_digit.txt
otp_6_digit.txt
```

---

### 🔹 Option 5: Common Wordlist Links

Provides links to popular community wordlists:

* SecLists
* RockYou
* CrackStation
* Probable Wordlists

---

## 📁 Output Handling

* All wordlists are:

  * **Deduplicated**
  * **Randomized**
  * **UTF‑8 encoded**
* Safe to use with tools like:

  * `hydra`
  * `hashcat`
  * `john`
  * `burpsuite`

---

## 🔒 Ethical Usage

✔ Allowed:

* Personal lab testing
* CTF challenges
* Authorized penetration tests
* Learning password security

❌ Not Allowed:

* Attacking real systems without permission
* Illegal access attempts

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**CoderKitty 🛡️**
Security Researcher | Ethical Hacker | Open‑Source Enthusiast

---

⭐ If you find WordDash useful, consider giving it a **star** on GitHub!
