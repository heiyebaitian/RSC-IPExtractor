import re
import requests

def extract_ip_addresses(url, output_file=None):
    ip_list = []
    pattern = re.compile(r'dst-address=([\d\./]+)')

    # 发送请求获取文件内容
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200，抛出异常
    except requests.RequestException as e:
        print(f"下载文件失败: {e}")
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


if __name__ == '__main__':
    rsc_url = 'http://ros.tcp5.com/table/unicom_latest.rsc'
    output_txt_file = 'extracted_ips.txt'

    extract_ip_addresses(rsc_url, output_txt_file)