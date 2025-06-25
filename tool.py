import re
import sys
import requests
import argparse

def extract_ip_addresses(url, output_file=None):
    ip_list = []
    pattern = re.compile(r'dst-address=([\d\./]+)')

    # 发送请求获取文件内容
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"下载IP列表失败: {e}")
        return

    # 处理响应文本
    for line in response.text.splitlines():
        if 'add action=lookup' in line:
            match = pattern.search(line)
            if match:
                ip_list.append(match.group(1))

    result = ';'.join(ip_list)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(result)
        print(f"结果已写入: {output_file}")
    else:
        print(result)

# 主程序
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="从 tcp5.com 远程服务器下载 .rsc 文件并提取 IP 地址便于Unifi策略路由导入")
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('-u', '--unicom', action='store_true', help='下载 unicom_latest.rsc (联通)')
    group.add_argument('-t', '--telecom', action='store_true', help='下载 telecom_latest.rsc (电信)')
    group.add_argument('-m', '--mobile', action='store_true', help='下载 mobile_latest.rsc (移动)')
    
    parser.add_argument('-o', '--output', type=str, help='指定输出文件路径（可选）')

    # 没有传入任何参数，显示帮助信息
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    base_url = "http://ros.tcp5.com/table/"

    if args.unicom:
        url = base_url + "unicom_latest.rsc"
        print("您选择了 联通 路由表")
    elif args.telecom:
        url = base_url + "telecom_latest.rsc"
        print("您选择了 电信 路由表")
    elif args.mobile:
        url = base_url + "mobile_latest.rsc"
        print("您选择了 移动 路由表")

    # 如果未指定输出文件，则使用默认值
    output_file = args.output if args.output else 'IPlist.txt'
    extract_ip_addresses(url, output_file)