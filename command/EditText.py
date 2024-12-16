from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *
from HtmlEditor import HtmlEditor
from command.Command import Command


class EditTextCommand(Command):
    def __init__(self, editor, node_id, new_text):
        self.editor = editor
        self.node_id = node_id
        self.node = self.editor.find_id(node_id)
        self.old_text = self.node.text
        self.new_text = new_text

    def execute(self):
        self.executed = True
        if self.node is None:
            return 1
        else:
            self.node.text = self.new_text
            return 0

    def undo(self):
        if self.executed:
            self.node.text = self.old_text
        self.executed = False

    def redo(self):
        if not self.executed:
            self.execute()
        self.executed = True
