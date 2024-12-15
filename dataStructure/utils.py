import re


SPECIAL_NAMES = ["html", "head", "body", "title"]


def get_html_text(html_str):
    # 匹配第一个 '<' 和 '>' 之间的内容
    match = re.search(r'>(.*?)<', html_str, re.DOTALL)
    if match:
        return match.group(1)  # 返回第一个捕获组中的内容
    return None  # 如果没有找到匹配，返回None

