class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        flag = command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()
        return flag

    def undo_command(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
            print("撤销成功")
        else:
            print("无可撤销操作")

    def redo_command(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.redo()
            self.undo_stack.append(command)
            print("重做成功")
        else:
            print("无可重做操作")
