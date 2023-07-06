import re
import os

import textract


def process_file(file_name: str):
    base_dir = os.getcwd()
    text = textract.process(f'{base_dir}/{file_name}')
    text = text.decode()
    return text


stack_over_flow_pattern = r'منابع و مآخذ[\n]*[^\S\r\n]*.*(?:\r?\n(?!\r?\n).*)+'

txt = process_file("پایان نامه شادی پورقدیری.docx")
matches = re.findall(r'منابع و مآخذ[\n]+[\s\S]*', txt)[0]
# matches = re.findall(r'منابع و مآخذ[\n]*', txt)[0]
# matches = matches.replace("منابع و مآخذ", "")
pieces = matches.split("]")
new_matches = "]".join(pieces[:-1])
last_piece = pieces[-1].split("\n\n\n")[0]
matches = "]".join([new_matches, last_piece])
print('matches:' + matches.split("\n\n\n")[0])
print("ok")
