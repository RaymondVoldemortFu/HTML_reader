class HtmlNode(object):
    def __init__(self, tag='', text='', id='', children=None, parent=None):
        if children is None:
            self.children = []
        else:
            self.children = children
        self.tag = tag
        self.text = text
        self.id = id
        self.parent = parent

    def add_child(self, child_node):
        """
        add a child node
        :param child_node:
        :return:
        """
        self.children.append(child_node)

    def get_tag(self):
        return self.tag

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def get_children(self):
        return self.children

    def __repr__(self):
        return f"<{self.tag} id={self.id}>{self.text}</{self.tag}>, parent_tag={self.parent.tag}"

    # def __str__(self):
    #    return f"<{self.tag} id={self.id}>{self.text}</{self.tag}>"
