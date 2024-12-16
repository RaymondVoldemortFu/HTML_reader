from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *
from HtmlEditor import HtmlEditor
from command.Command import Command


class EditIdCommand(Command):
    def __init__(self, editor, old_id, new_id):
        self.editor = editor
        self.old_id = old_id
        self.new_id = new_id
        self.node = self.editor.find_id(self.old_id)

    def execute(self):
        self.executed = True
        if self.node is None:
            return 1
        if self.editor.find_id(self.new_id) is not None:
            return 2
        else:
            self.node.id = self.new_id
            return 0

    def undo(self):
        if self.executed:
            self.node.id = self.old_id
        self.executed = False

    def redo(self):
        if not self.executed:
            self.execute()
        self.executed = True
