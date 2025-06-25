import re

def extract_ip_addresses(file_path, output_file=None):
    ip_list = []
    pattern = re.compile(r'dst-address=([\d\./]+)')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
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
    input_rsc_file = 'unicom_latest.rsc'
    output_txt_file = 'extracted_ips.txt'

    extract_ip_addresses(input_rsc_file, output_txt_file)