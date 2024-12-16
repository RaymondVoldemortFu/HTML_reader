from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *


class HtmlEditor:
    def __init__(self, html_doc: HtmlDocument = None):
        self.HtmlDoc = html_doc

    def read_html_file(self, file_path):
        self.HtmlDoc = parse_html_file(file_path=file_path)

    def write_html_file_indent(self, file_path, indent=2):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.HtmlDoc.to_html_indent_string(self.HtmlDoc.html, 0, indent))

    def find_tag(self, tag: str):
        return self.HtmlDoc.find_tag(tag)

    def find_id(self, id: str):
        return self.HtmlDoc.find_id(id)

    def insert_node_before(self, node: HtmlNode, before_node: HtmlNode):
        parent = before_node.parent
        index = parent.children.index(before_node)
        parent.children.insert(index, node)
        self.HtmlDoc.thread_initialize()

    def insert_node_tag_id_before_id(self, node_tag: str, node_id: str, before_id: str, text: str = ''):
        if before_id == node_id:
            return 1
        node = HtmlNode(tag=node_tag, id=node_id, text=text)
        before_node = self.find_id(before_id)
        if before_node is None:
            return 2
        self.insert_node_before(node, before_node)
        return 0

    def insert_node_at_index_parent(self, index: int, node: HtmlNode, parent: HtmlNode):
        parent.children.insert(index, node)

    def append_node_in_parent(self, node: HtmlNode, parent: HtmlNode):
        if parent is None:
            return False
        parent.children.append(node)
        node.parent = parent
        self.HtmlDoc.thread_initialize()
        return True

    def append_node_tag_id_parent_id(self, node_tag: str, node_id: str, parent_id: str, text: str = ''):
        if node_id == parent_id:
            return 1
        node = HtmlNode(tag=node_tag, id=node_id, text=text)
        parent = self.find_id(parent_id)
        if parent is None:
            return 2
        self.append_node_in_parent(node, parent)
        return 0

    def append_node_parent_id(self, node: HtmlNode, parent_id: str):
        if node.id == parent_id:
            return 1
        parent = self.find_id(parent_id)
        if parent is None:
            return 2
        self.append_node_in_parent(node, parent)
        return 0

    def delete_node_id(self, node_id: str):
        node = self.find_id(node_id)
        if node is None:
            return 1
        parent = node.parent
        if node_id == "html":
            self.HtmlDoc = None
            return True
        if parent is None:
            return 2
        parent.children.remove(node)
        return 0

    def replace_node_id(self, old_id: str, new_id: str):
        node = self.find_id(old_id)
        if node is None:
            return 1
        same_id_node = self.find_id(new_id)
        if same_id_node is not None:
            return 2
        node.id = new_id
        return 0

    def edit_node_id_text(self, node_id: str, text: str):
        node = self.find_id(node_id)
        if node is None:
            return False
        node.text = text
        return True

    def save_document(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.HtmlDoc.to_html_indent_string(self.HtmlDoc.html, 0, 2))
