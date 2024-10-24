
# BL Checker 🛡️

Python script that allows you to analyze `IP addresses`, `domain names`, `URLs`, and `files` to check their presence in threat blacklists. It also includes an update feature to ensure that the databases used are always up-to-date with the latest information.

## 💫 Features

* IP, Domain, URL, and File Analysis:
The script allows you to check if an IP address, domain, URL, or file (via its SHA-256 hash) is listed in any threat blacklist.

* Database Update:
Using the --update command, the script downloads and updates the blacklist files for IPs, domains, URLs, and file hashes.

* Security Reports:
When a match is found, the script generates an alert identifying the type of threat.

## 🎃 Usage Demo

![demo]

  ```sh
  python3 main.py -t [ip | domain | url | file] -s [source]
  ```
  * Options :
`-u` or `--update`: Downloads and updates the blacklist databases before analysis.  
`-t` or `--type`: Specifies the type of source to analyze (IP, domain, URL, or file).  
`-s` or `--source`: Indicates the source to analyze (IP address, domain name, etc.).    

## 📂 Installation

`pip install -r requirements.txt`  
Make sure you are in the directory where the requirements.txt file is located.

Ensure Python is properly installed on your system by running `python --version` or `python3 --version` in your terminal.

## 💻 Author

piairlika

<!-- MARKDOWN LINKS -->

[demo]: https://pouch.jumpshare.com/preview/3tPoKwB25IqxfG9akCIZdXb4pgVa12G80ru959oRPlG1gAFRSbhY2S8dOKh6OeQwkJ03l0Kkgrzh5hMx_dn1WPnISDjqxNvphql1zHr05Ow