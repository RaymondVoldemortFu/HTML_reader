from dataStructure.HtmlDocument import *
from dataStructure.HtmlNode import *
from HtmlEditor import HtmlEditor
from command.Command import Command


class InsertCommand(Command):
    def __init__(self, editor, node_tag, node_id, before_id, text):
        self.editor = editor
        self.node_tag = node_tag
        self.node_id = node_id
        self.before_id = before_id
        self.text = text
        self.executed = False

    def execute(self):
        self.executed = True
        return self.editor.insert_node_tag_id_before_id(node_tag=self.node_tag, node_id=self.node_id,
                                                 before_id=self.before_id, text=self.text)

    def undo(self):
        if self.executed:
            self.editor.delete_node_id(self.node_id)
        self.executed = False

    def redo(self):
        if not self.executed:
            self.execute()
        self.executed = True

    def __repr__(self):
        return f"nodetag{self.node_tag}_id{self.node_id}_before{self.before_id} text:{self.text} executed:{self.executed}"