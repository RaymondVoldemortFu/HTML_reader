from dataStructure.HtmlNode import HtmlNode
from dataStructure.utils import get_html_text, SPECIAL_NAMES
from collections import deque
from bs4 import BeautifulSoup


class HtmlDocument:
    def __init__(self, title_text=''):
        """
        initialize a Html Document
        :param title_text:
        """
        self.html = HtmlNode(tag='html', id='html')
        self.head = HtmlNode(tag='head', id='head')
        self.title = HtmlNode(tag='title', id='title', text=title_text)
        self.body = HtmlNode(tag='body', id='body')

        # title is child of head
        self.head.add_child(self.title)

        # head and body is child of html
        self.html.add_child(self.head)
        self.html.add_child(self.body)

    def add_to_body(self, node):
        self.body.add_child(node)
        self.thread_initialize()

    def __repr__(self):
        return (f"HtmlDocument(html={repr(self.html)}, head={repr(self.head)},"
                f" title={repr(self.title)}, body={repr(self.body)})")

    def find_tag(self, tag: str):
        q = deque()
        q.append(self.html)
        result = []
        while q:
            node = q.popleft()
            if node.tag == tag:
                result.append(node)
            for child in node.children:
                q.append(child)
        return result

    def find_id(self, id: str):
        q = deque()
        q.append(self.html)
        while q:
            node = q.popleft()
            if node.id == id:
                return node
            for child in node.children:
                q.append(child)
        return None

    def thread_initialize(self):
        """
        线索化html树结构
        :return:
        """
        self.html.parent = None

        self.head.parent = self.html
        self.body.parent = self.html

        self.title.parent = self.head
        q = deque()
        q.append(self.body)
        while q:
            node = q.popleft()
            for child in node.children:
                q.append(child)
                child.parent = node

    def print_tree(self, node=None, prefix='', is_last=False, is_first=True):
        """
        print the tree of html document recursively
        :param node:
        :param prefix:
        :param is_last:
        :param is_first:
        :return:
        """
        if node is None:
            node = self.html

        # 打印当前节点
        print(prefix, end='')  # 打印前缀
        if is_first:
            pass
        elif is_last:
            print("└── ", end='')  # 最后一个子节点
        else:
            print("├── ", end='')  # 普通子节点

        # 打印节点的标签名
        print(node.get_tag(), end='')

        # 只有当 ID 不为空且不是特殊标签时，才打印 ID
        if node.get_id() and node.get_id().strip() and node.get_id() not in SPECIAL_NAMES:
            print(f"#{node.get_id()}", end='')

        print()  # 换行

        # 如果有文本内容，输出文本内容（作为子节点）
        if node.get_text() and node.get_text().strip():
            print(prefix, end='')
            if is_last:
                print("    ", end='')  # 对齐最后一个子节点
            else:
                print("│   ", end='')  # 对齐普通子节点
            print(f"└── {node.get_text().strip()}")

        # 获取子节点列表
        children = node.get_children()
        child_count = len(children)
        if is_first:
            pass
        elif is_last:
            prefix += "    "
        else:
            prefix += "│   "
        for i, child in enumerate(children):
            # 递归打印子节点
            self.print_tree(node=child, prefix=prefix, is_last=i == child_count - 1, is_first=False)

    def print_indent(self, n=2):
        print(self.to_html_indent_string(node=self.html, indent_level=0, indent_number=n))

    def to_html_indent_string(self, node, indent_level, indent_number=2):
        """递归转换 HtmlNode 为缩进格式的 HTML 字符串"""
        indent_space = ' ' * indent_number
        indent = indent_space * indent_level  # 每层缩进两个空格
        html_str = f"{indent}<{node.tag}"

        if node.get_tag() in SPECIAL_NAMES:
            pass
        elif node.id:
            html_str += f' id="{node.id}"'

        html_str += ">"

        # 添加文本内容（如果有）
        if node.text:
            html_str += f"{node.text}"

        # 递归处理子节点
        if node.children:
            html_str += "\n"
            for child in node.children:
                html_str += self.to_html_indent_string(child, indent_level + 1) + "\n"

            html_str += f"{indent}"  # 关闭标签前的缩进

        html_str += f"</{node.tag}>"

        return html_str


def parse_html_file(file_path):
    """
    read html file and parse html document
    :param file_path:
    :return: HtmlDocument
    """
    # 读取 HTML 文件
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'lxml')

    # 读取 <title> 标签内容
    title_text = soup.title.string if soup.title else "No Title"

    # 创建 HtmlDocument 实例
    doc = HtmlDocument(title_text)

    # 遍历 <body> 中的内容并添加到 HtmlDocument
    body = soup.body
    if body:
        # 递归遍历 body 内容并构建节点
        def process_node(soup_node):
            if soup_node.name:
                # 创建当前节点
                node_id = soup_node.get('id')
                text = get_html_text(str(soup_node))
                # text = soup_node.get_text(strip=True)
                node = HtmlNode(tag=soup_node.name, id=node_id, text=text)

                # 递归处理子节点
                for child in soup_node.children:
                    child_node = process_node(child)
                    if child_node:
                        node.add_child(child_node)

                return node
            return None

        # 处理 body 中的每一个子节点
        for child in body.children:
            child_node = process_node(child)
            if child_node:
                doc.add_to_body(child_node)
    doc.thread_initialize()
    return doc


# doc = parse_html_file(r"D:\CS\dataStructure\FDU\project2\HTML_reader\html_files\example.html")
# doc.print_tree()
# print()
# doc.print_indent()

# docu = HtmlDocument()
docu = parse_html_file(r"D:\CS\dataStructure\FDU\project2\HTML_reader\html_files\example.html")
docu.print_indent()
# print(docu.find_tag("html")[0])
print(docu.find_id("copyright"))
