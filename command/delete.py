from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *
from HtmlEditor import HtmlEditor
from command.Command import Command


class DeleteCommand(Command):
    def __init__(self, editor, node):
        self.editor = editor
        self.node = node
        if node is None:
            self.parent = None
        else:
            self.parent = node.parent
        self.executed = False
        if self.parent is None:
            self.is_root = True
            self.index = 0
        else:
            self.is_root = False
            self.index = self.parent.children.index(self.node)

    def execute(self):
        self.executed = True
        if self.node is None:
            return 1
        return self.editor.delete_node_id(self.node.id)

    def undo(self):
        if self.executed:
            self.editor.insert_node_at_index_parent(index=self.index, node=self.node, parent=self.parent)
        self.executed = False

    def redo(self):
        if not self.executed:
            self.execute()
        self.executed = True
