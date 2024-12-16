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

    def insert_node_before(self, node: HtmlNode):
