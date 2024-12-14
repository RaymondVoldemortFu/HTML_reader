from dataStructure.HtmlNode import HtmlNode
from collections import deque


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

    def __repr__(self):
        return (f"HtmlDocument(html={repr(self.html)}, head={repr(self.head)},"
                f" title={repr(self.title)}, body={repr(self.body)})")

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
        if node.get_id() and node.get_id().strip() and node.get_id() not in ["html", "head", "body", "title"]:
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


document = HtmlDocument()
document.print_tree()
