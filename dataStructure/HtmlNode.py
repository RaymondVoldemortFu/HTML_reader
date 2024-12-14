class HtmlNode(object):
    def __init__(self, tag='', text='', id='', children=None):
        if children is None:
            self.children = []
        else:
            self.children = children
        self.tag = tag
        self.text = text
        self.id = id

    def add_child(self, child_node):
        """
        add a child node
        :param child_node:
        :return:
        """
        self.children.append(child_node)

    def __repr__(self):
        return f"HtmlNode(tag='{self.tag}', id='{self.id}', text='{self.text}', children={len(self.children)})"

