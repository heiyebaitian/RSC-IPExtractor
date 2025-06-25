# 🌐 RSC-IPExtractor
**Read this in other languages: [English](README.md), [中文](README_zh.md).**

## 📌 Overview
RSC-IPExtractor 是一个轻量级命令行工具，用于从 RouterOS 的 .rsc 配置脚本中提取 IP 地址列表。支持自动从远程服务器下载不同运营商（联通、电信、移动）的规则表，并将匹配到的 dst-address 提取为以分号分隔的字符串输出或保存至文件。

适用于网络管理、路由策略维护等场景，可快速获取黑名单、白名单或策略路由所需的 IP 列表。

此程序是笔者在尝试使用.rsc文件配置Unifi的策略路由时所写，为了解决无法直接导入IP表的问题。

## 🛠 功能特性
✅ 支持远程下载 .rsc 文件（无需手动本地存储）

✅ 自动识别并提取 dst-address 规则中的 IP 地址

✅ 支持选择运营商：
-u：联通（unicom）
-t：电信（telecom）
-m：移动（mobile）

✅ 可选输出文件，默认生成 IPlist.txt

✅ 无依赖（仅需 Python 标准库 + requests）

## 📦 安装与使用
安装依赖：

    pip install requests

运行示例：

    # Download China Unicom's rules and print IPs
    python rsc_ip_extractor.py -u

    # Download China Telecom's rules and save to custom file
    python rsc_ip_extractor.py -t -o telecom_ips.txt

    # Download China Mobile's rules with default output file
    python rsc_ip_extractor.py -m

显示帮助信息：

    python tool.py
