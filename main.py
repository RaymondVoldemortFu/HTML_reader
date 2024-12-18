from HtmlEditor import HtmlEditor
from dataStructure.HtmlDocument import *
from userInterface.utils import *
from command.CommandManager import CommandManager
from command.Command import Command
from command.insert import InsertCommand
from command.append import AppendCommand
from command.delete import DeleteCommand
from command.editId import EditIdCommand
from command.EditText import EditTextCommand


if __name__ == '__main__':
    editor = HtmlEditor()
    welcome()
    commandManager = CommandManager()
    while True:
        user_input = input('请输入命令: ')
        inputs = user_input.split(" ")
        command = inputs[0]
        match command:
            case "help":
                print_help()
            case "exit":
                exit(0)
            case "print-tree":
                if editor.HtmlDoc is None:
                    print("no html file")
                    continue
                else:
                    editor.HtmlDoc.print_tree()
            case "print-indent":
                if editor.HtmlDoc is None:
                    print("no html file")
                    continue
                if len(inputs) == 1:
                    editor.HtmlDoc.print_indent()
                elif len(inputs) == 2:
                    try:
                        num = int(inputs[1])
                        editor.HtmlDoc.print_indent(num)
                    except ValueError:
                        print("indent参数必须为数字")
                else:
                    print("非法指令: print-indent仅有一个参数")
            case "read":
                path = inputs[1]
                try:
                    editor.read_html_file(path)
                    print("已读取文件：" + path)
                except FileNotFoundError:
                    print("文件不存在")
                except OSError:
                    print("文件路径错误")
            case "save":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                path = inputs[1]
                try:
                    editor.save_document(path)
                    print("已保存到文件" + path)
                except FileNotFoundError:
                    print("路径错误")
                except OSError:
                    print("文件路径格式错误")
            case "init":
                editor.HtmlDoc = HtmlDocument()
                print("successfully initialize html file")
            case "find-id":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                id = inputs[1]
                node = editor.HtmlDoc.find_id(id)
                if node is None:
                    print("id不存在")
                else:
                    print(node)
            case "find-tag":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                tag = inputs[1]
                nodes = editor.HtmlDoc.find_tag(tag)
                if len(nodes) == 0:
                    print("tag不存在")
                else:
                    for node in nodes:
                        print(node)
            case "insert":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                if len(inputs) < 4:
                    print("非法输入")
                    continue
                tag = inputs[1]
                new_node_id = inputs[2]
                before_id = inputs[3]
                text = ''
                if len(inputs) >= 5:
                    for i in range(4, len(inputs)):
                        text += inputs[i]
                        if i != len(inputs) - 1:
                            text += ' '
                insert = InsertCommand(editor=editor, node_tag=tag, node_id=new_node_id, before_id=before_id, text=text)
                flag = commandManager.execute_command(insert)
                if flag == 1:
                    commandManager.undo_stack.pop()
                    print("新节点id不可与旧节点相同")
                elif flag == 2:
                    commandManager.undo_stack.pop()
                    print("指定节点不存在")
                elif flag == 0:
                    print(f"节点id={new_node_id}插入成功")
                else:
                    commandManager.undo_stack.pop()
                    print("error")
            case "append":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                if len(inputs) < 4:
                    print("非法输入")
                    continue
                tag = inputs[1]
                new_node_id = inputs[2]
                parent_id = inputs[3]
                text = ''
                if len(inputs) >= 5:
                    for i in range(4, len(inputs)):
                        text += inputs[i]
                        if i != len(inputs) - 1:
                            text += ' '
                # breakpoint()
                append = AppendCommand(editor=editor, node_tag=tag, node_id=new_node_id, parent_id=parent_id, text=text)
                flag = commandManager.execute_command(append)
                if flag == 1:
                    commandManager.undo_stack.pop()
                    print("新节点id不可与旧节点相同")
                elif flag == 2:
                    commandManager.undo_stack.pop()
                    print("指定节点不存在")
                elif flag == 0:
                    print(f"节点id={new_node_id}插入成功")
                else:
                    commandManager.undo_stack.pop()
                    print("error: unhandled exception in append")
            case "delete":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                id = inputs[1]
                # breakpoint()
                delete = DeleteCommand(editor=editor, node=editor.find_id(id))
                flag = commandManager.execute_command(delete)
                if flag == 1:
                    print("指定节点不存在")
                    commandManager.undo_stack.pop()
                elif flag == 2:
                    print("错误: 父节点不存在")
                    commandManager.undo_stack.pop()
                elif flag == 0:
                    print(f"节点id={id}删除成功")
                else:
                    print("error: unhandled exception in delete")
                    commandManager.undo_stack.pop()
            case "edit-id":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                if len(inputs) != 3:
                    print("缺少参数: edit-id需要两个参数, 输入\"help\"查看详情")
                    continue
                old_id = inputs[1]
                new_id = inputs[2]
                edit_id = EditIdCommand(editor=editor, old_id=old_id, new_id=new_id)
                flag = commandManager.execute_command(edit_id)
                if flag == 1:
                    commandManager.undo_stack.pop()
                    print("节点不存在")
                elif flag == 2:
                    commandManager.undo_stack.pop()
                    print("新id已存在")
                elif flag == 0:
                    print(f"id {old_id} 已替换为 {new_id}")
                else:
                    print("error: unhandled exception in edit-id")
            case "edit-text":
                if editor.HtmlDoc is None:
                    print("no html file!")
                    continue
                if len(inputs) < 2:
                    print("缺少参数: edit-text需要至少一个参数, 输入\"help\"查看详情")
                    continue
                id = inputs[1]
                text = ''
                if len(inputs) >= 5:
                    for i in range(2, len(inputs)):
                        text += inputs[i]
                        if i != len(inputs) - 1:
                            text += ' '
                edit_text = EditTextCommand(editor=editor, node_id=id, new_text=text)
                flag = commandManager.execute_command(edit_text)
                if flag == 1:
                    commandManager.undo_stack.pop()
                    print("指定节点不存在")
                    continue
                elif flag == 0:
                    print(f"已编辑id {id}节点文本")
                else:
                    commandManager.undo_stack.pop()
                    print("error: unhandled exception in edit-text")
            case "undo":
                # breakpoint()
                commandManager.undo_command()
            case "redo":
                commandManager.redo_command()
            case _:
                print("非法指令, 输入\"help\"查看帮助")
