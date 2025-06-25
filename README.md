# 🌐 RSC-IPExtractor
**Read this in other languages: [English](README.md), [中文](README_zh.md).**

## 📌 Overview
RSC-IPExtractor is a lightweight CLI tool designed to extract IP addresses from RouterOS .rsc configuration scripts. It supports downloading rule sets from remote URLs for different Chinese ISPs (China Unicom, China Telecom, China Mobile), and extracts the dst-address entries into a semicolon-separated string output or saves them to a file.

Ideal for network management, firewall rules, routing policies, and more.

## 🛠 Features
✅ Download .rsc files directly from remote URLs

✅ Extracts dst-address fields matching IP addresses

✅ Choose ISP via command line:
-u for China Unicom
-t for China Telecom
-m for China Mobile

✅ Optional output file, defaults to IPlist.txt

✅ Minimal dependencies (only uses requests)

## 📦 Installation & Usage
Install Dependencies:

    pip install requests

Examples:

    # Download China Unicom's rules and print IPs
    python rsc_ip_extractor.py -u

    # Download China Telecom's rules and save to custom file
    python rsc_ip_extractor.py -t -o telecom_ips.txt

    # Download China Mobile's rules with default output file
    python rsc_ip_extractor.py -m

Show Help:

    python tool.py
