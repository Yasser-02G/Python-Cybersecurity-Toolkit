# 🐍 Python Cybersecurity & Tools Toolkit

> A collection of Python scripts covering core concepts in **cybersecurity**, **network reconnaissance**, **web exploitation**, **reverse engineering**, and **Python utilities** — built for educational purposes and hands-on learning.

---

## 📁 Project Structure

```
Python projects/
│
├── 🔴 Exploit & Brute/
│   ├── brute_force_attack.py     # Automated login brute-force via Playwright
│   ├── forms.py                  # Web form enumeration
│   ├── sql.py                    # SQL injection detection
│   └── xss.py                   # XSS payload testing (20+ payloads)
│
├── 🟠 Lan Attacking/
│   └── MITM.py                   # ARP spoofing + DNS sniffing (Man-in-the-Middle)
│
├── 🟡 Reconnaissance/
│   ├── statut.py                 # HTTP status check (site up/down)
│   ├── server_info.py            # HTTP header enumeration
│   ├── site_technology.py        # Technology stack fingerprinting
│   ├── dns_reolution.py          # DNS resolution (domain → IP)
│   ├── domain_info.py            # WHOIS lookup via API
│   ├── file_intraction.py        # Remote file download/interaction
│   ├── get.py                    # HTTP GET request + JSON export
│   ├── send.py                   # HTTP POST request
│   ├── data.json                 # Sample JSON output
│   └── data.sql                  # Sample SQL schema (Acuart vuln app)
│
├── 🔵 Reverse Engineering/
│   ├── Camouflage/
│   │   ├── new.py                # Obfuscated Python (marshal hex-encoded exec)
│   │   ├── test.py               # Baseline plain script
│   │   └── 1.json                # Sample data file
│   ├── Cryptage/
│   │   ├── bytecode.py           # Compiles .py → .pyc bytecode
│   │   ├── new_scripte1.pyc      # Compiled bytecode output
│   │   ├── new_scripte2.py       # Reads & inspects .pyc with dis.code_info
│   │   ├── new_scripte3.py       # Disassembles .pyc bytecode with dis.dis
│   │   └── scripte.py            # Source script used for compilation
│   └── Marshal/
│       ├── marshal.py            # Interactive marshal encode/decode from stdin
│       ├── marshal_file1.py      # Serialize .py file → marshal binary (new.py)
│       ├── marshal_file2.py      # Deserialize marshal binary → readable output
│       └── scripte.py            # Source script used for marshal demos
│
└── 🟢 Python Tools/
    ├── app.py                    # CLI multi-tool with argparse (tool1, tool2)
    ├── arg.py                    # Argparse hello-world example
    ├── QR.py                     # QR code generator (Instagram link → PNG)
    ├── QR.png                    # Generated QR code output
    ├── sp_recognition.py         # Voice command recognition (Google Speech API)
    ├── speed_test.py             # Internet speed test (download/upload)
    ├── TTS.py                    # Text-to-Speech engine with voice selection
    └── new.jpg                   # Sample image asset
```

---

## 🛠️ Tools & Technologies

| Category             | Tool / Technology                                     | Role                                          |
| -------------------- | ----------------------------------------------------- | --------------------------------------------- |
| Language             | **Python 3**                                          | All scripts                                   |
| Browser Automation   | **Playwright**                                        | Brute-force, form enumeration, XSS testing    |
| Network Manipulation | **Scapy**                                             | ARP spoofing, DNS packet sniffing (MITM)      |
| HTTP Requests        | **Requests**                                          | Reconnaissance, API calls, file download      |
| Terminal Output      | **Rich**                                              | Colored and styled CLI output                 |
| Threading            | **threading**                                         | Parallel ARP spoofing loop                    |
| CLI Parsing          | **argparse**                                          | Multi-tool command-line interface (`app.py`)  |
| Bytecode             | **py_compile / marshal / dis**                        | Python bytecode compilation and disassembly   |
| QR Code              | **qrcode**                                            | QR code image generation                      |
| Speech Recognition   | **SpeechRecognition**                                 | Microphone input + Google Speech-to-Text API  |
| Speed Test           | **speedtest-cli**                                     | Measure internet download/upload speed        |
| Text-to-Speech       | **pyttsx3**                                           | Offline TTS engine with voice and rate config |
| Target App           | **[testphp.vulnweb.com](http://testphp.vulnweb.com)** | Intentionally vulnerable web app (Acunetix)   |
| REST API             | **jsonplaceholder.typicode.com**                      | GET/POST request testing                      |
| WHOIS API            | **api.whois.vu**                                      | Domain information lookup                     |

---

## 📌 Key Concepts Covered

### 🔴 Exploit & Brute

- **Brute-force attack** — automates login attempts on a web form using Playwright (headless Chromium) with a username and password wordlist; stops immediately on success
- **Form enumeration** — scrapes and prints all HTML `<form>` elements from a target page to identify attack surfaces
- **SQL injection detection** — sends payloads (`'`, `\`) appended to URL parameters and compares page responses to detect vulnerable inputs
- **XSS testing** — injects 20+ real-world XSS payloads (event handlers, SVG vectors, encoded variants) into search fields and checks if they are reflected in the DOM

### 🟠 LAN Attacking

- **ARP Spoofing** — crafts and continuously sends ARP reply packets to poison the ARP tables of both a target and its gateway, positioning the attacker as a Man-in-the-Middle
- **DNS Sniffing** — uses Scapy to filter UDP port 53 traffic and print all DNS queries made by the target in real time, revealing every domain they try to resolve

### 🟡 Reconnaissance

- **HTTP status monitoring** — sends a GET request and reports whether a target is online (`200 OK`) or unreachable
- **Server fingerprinting** — reads all HTTP response headers (`Server`, `X-Powered-By`, `Content-Type`, etc.) from a HEAD request to identify server software
- **Technology enumeration** — queries a target and parses its headers to fingerprint the technology stack using the `Rich` library for styled output
- **DNS resolution** — resolves a user-supplied domain name to its IP address using `socket.gethostbyname`
- **WHOIS lookup** — queries `api.whois.vu` to retrieve domain registration data (owner, registrar, dates)
- **Remote file interaction** — downloads files exposed on a web server (e.g., `.sql` schema files) and saves them locally
- **REST API interaction** — demonstrates GET (with JSON file export) and POST requests against a public JSON API

### 🔵 Reverse Engineering

**Camouflage**

- **Code obfuscation** — demonstrates hiding Python source code using `marshal.dumps` to serialize compiled code objects into binary, then embedding them in a hex-encoded `exec()` chain to make static analysis difficult

**Cryptage (Bytecode)**

- **Bytecode compilation** — uses `py_compile.compile()` to convert a `.py` source file into a `.pyc` bytecode file
- **Bytecode inspection** — reads a `.pyc` file (skipping the 16-byte magic header), deserializes the code object with `marshal.loads`, and prints structured code info using `dis.code_info`
- **Bytecode disassembly** — uses `dis.dis` to produce a full human-readable disassembly of compiled bytecode, revealing the original instruction sequence

**Marshal**

- **Interactive marshal encode/decode** — takes user input code as a string, compiles and serializes it with `marshal.dumps`, then deserializes and executes it with `exec` to demonstrate the full encode/decode cycle
- **File-based serialization** — reads a `.py` source file, marshals the compiled code object to a binary file (`new.py`), then deserializes it back to a readable string in a separate file (`dec.py`)

### 🟢 Python Tools

- **CLI multi-tool** — uses `argparse` to build a command-line interface with subcommands (`tool1`, `tool2`), demonstrating how to structure a Python CLI application
- **QR code generation** — generates a QR code image from a URL (Instagram profile) using the `qrcode` library and saves it as a PNG
- **Voice command recognition** — listens to microphone input in a loop, sends audio to Google's Speech-to-Text API, and responds to specific commands (`hello`, `how are you`, `stop`)
- **Internet speed test** — measures real-time download and upload speeds in Mbit/s using the `speedtest-cli` library
- **Text-to-Speech (TTS)** — initializes `pyttsx3`, lists all available system voices, lets the user select one and set speech rate, then reads text aloud or saves it to an audio file

---

## ⚙️ Installation

```bash
git clone https://github.com/Yasser-02G/python-cybersecurity-toolkit.git
cd python-cybersecurity-toolkit

# Install all dependencies
pip install playwright requests scapy rich qrcode pyttsx3 \
            SpeechRecognition speedtest-cli argparse

# Install Playwright browser engine
playwright install chromium
```

> **Note:** Scapy and the MITM module require **root/admin privileges** for raw packet operations.
> Run with `sudo python "Lan Attacking/MITM.py"` on Linux/macOS.

---

## 🚀 Usage

### 🔴 Exploit & Brute

```bash
# Brute-force a login form
python "Exploit & Brute/brute_force_attack.py"

# Enumerate all forms on a target page
python "Exploit & Brute/forms.py"

# Detect SQL injection in URL parameters
python "Exploit & Brute/sql.py"

# Test XSS payloads on a search field
python "Exploit & Brute/xss.py"
```

### 🟠 LAN Attacking

```bash
# Launch ARP spoofing + DNS sniffing (requires root/admin)
sudo python "Lan Attacking/MITM.py"
```

### 🟡 Reconnaissance

```bash
python "Reconnaissance/statut.py"          # Check site status
python "Reconnaissance/server_info.py"     # Read HTTP headers
python "Reconnaissance/site_technology.py" # Fingerprint tech stack
python "Reconnaissance/dns_reolution.py"   # Resolve domain → IP
python "Reconnaissance/domain_info.py"     # WHOIS lookup
python "Reconnaissance/file_intraction.py" # Download remote file
python "Reconnaissance/get.py"             # GET request + JSON export
python "Reconnaissance/send.py"            # POST request
```

### 🔵 Reverse Engineering

```bash
# --- Cryptage (Bytecode) ---
python "Reverse Engineering/Cryptage/bytecode.py"      # Compile scripte.py → .pyc
python "Reverse Engineering/Cryptage/new_scripte2.py"  # Inspect .pyc with dis.code_info
python "Reverse Engineering/Cryptage/new_scripte3.py"  # Disassemble .pyc with dis.dis

# --- Marshal ---
python "Reverse Engineering/Marshal/marshal.py"        # Interactive encode/decode
python "Reverse Engineering/Marshal/marshal_file1.py"  # Serialize .py → binary
python "Reverse Engineering/Marshal/marshal_file2.py"  # Deserialize binary → text
```

### 🟢 Python Tools

```bash
python "Python Tools/QR.py"                # Generate QR code → QR.png
python "Python Tools/sp_recognition.py"   # Voice command recognition
python "Python Tools/speed_test.py"       # Internet speed test
python "Python Tools/TTS.py"              # Text-to-Speech

# CLI multi-tool
python "Python Tools/app.py" help         # Show available commands
python "Python Tools/app.py" tool1        # Check vulnweb.com status
python "Python Tools/app.py" tool2        # Check any URL status
```

---

## 📸 Sample Output

**QR Code generated by `QR.py`** (links to Instagram profile):

![QR Code](Python%20Tools/QR.png)

---

## ⚠️ Legal Disclaimer

> **This project is strictly for educational and research purposes.**
>
> All attack scripts are tested exclusively against **intentionally vulnerable environments**
> (such as [testphp.vulnweb.com](http://testphp.vulnweb.com), officially provided by Acunetix
> for legal penetration testing practice) or isolated lab networks under the author's own control.
>
> **Do NOT** use any of these tools against systems you do not own or have explicit written
> permission to test. Unauthorized use may be illegal under applicable laws (CFAA, Computer
> Misuse Act, etc.).
>
> The author takes no responsibility for any misuse of this code.

---

## 👤 Author

**Yasser**

- GitHub: [@Yasser-02G](https://github.com/Yasser-02G)
- Instagram: [@yasser*02*](https://www.instagram.com/yasser_02_/)

Feel free to open an _issue_ or _pull request_ for suggestions or improvements.

---

## 📄 License

Distributed under the MIT License.
