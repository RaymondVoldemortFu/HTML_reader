from dataStructure.HtmlNode import HtmlNode


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



