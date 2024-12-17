from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *
from HtmlEditor import HtmlEditor
from command.Command import Command


class AppendCommand(Command):
    def __init__(self, editor, node_tag, node_id, parent_id, text):
        self.editor = editor
        self.node_tag = node_tag
        self.node_id = node_id
        self.parent_id = parent_id
        self.text = text
        self.node = None
        self.executed = False

    def execute(self):
        parent = self.editor.find_id(self.parent_id)
        node = self.editor.find_id(self.node_id)
        if node is not None:
            return 1
        self.node = HtmlNode(tag=self.node_tag, id=self.node_id, text=self.text, parent=parent)
        self.executed = True
        return self.editor.append_node_parent_id(node=self.node, parent_id=self.parent_id)

    def undo(self):
        # breakpoint()
        if self.node and self.node.parent:
            self.node.parent.children.remove(self.node)
            self.node.parent = None
        self.executed = False

    def redo(self):
        parent = self.editor.find_id(self.parent_id)
        if parent:
            self.editor.append_node_in_parent(self.node, parent)
        self.executed = True
