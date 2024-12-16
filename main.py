from HtmlEditor import HtmlEditor
from dataStructure.HtmlDocument import *
from userInterface.utils import *

if __name__ == '__main__':
    editor = HtmlEditor()
    welcome()
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
                editor.HtmlDoc.print_tree()
            case "print-indent":
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
                except FileNotFoundError:
                    print("文件不存在")
            case "save":
                path = inputs[1]
                editor.save_document(path)
            case "init":
                editor.HtmlDoc = HtmlDocument()
            case "find-id":
                id = inputs[1]
                node = editor.HtmlDoc.find_id(id)
                if node is None:
                    print("id不存在")
                else:
                    print(node)
            case "find-tag":
                tag = inputs[1]
                nodes = editor.HtmlDoc.find_tag(tag)
                if len(nodes) == 0:
                    print("tag不存在")
                else:
                    for node in nodes:
                        print(node)
            case "insert":
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
                flag = editor.insert_node_tag_id_before_id(node_tag=tag, node_id=new_node_id,
                                                           before_id=before_id, text=text)
                if flag == 1:
                    print("新节点id不可与旧节点相同")
                elif flag == 2:
                    print("指定节点不存在")
                elif flag == 0:
                    print(f"节点id={new_node_id}插入成功")
                else:
                    print("error")
            case "append":
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
                flag = editor.append_node_tag_id_parent_id(node_tag=tag, node_id=new_node_id,
                                                           parent_id=parent_id, text=text)
                if flag == 1:
                    print("新节点id不可与旧节点相同")
                elif flag == 2:
                    print("指定节点不存在")
                elif flag == 0:
                    print(f"节点id={new_node_id}插入成功")
                else:
                    print("error: unhandled exception in insert")
            case "delete":
                id = inputs[1]
                flag = editor.delete_node_id(id)
                if flag == 1:
                    print("指定节点不存在")
                elif flag == 2:
                    print("错误: 父节点不存在")
                elif flag == 0:
                    print(f"节点id={id}插入成功")
                else:
                    print("error: unhandled exception in append")
            case "edit-id":
                if len(inputs) != 3:
                    print("缺少参数: edit-id需要两个参数, 输入\"help\"查看详情")
                    continue
                old_id = inputs[1]
                new_id = inputs[2]
                node = editor.HtmlDoc.find_id(old_id)
                if node is None:
                    print("指定节点不存在")
                    continue
                else:
                    node.id = new_id
            case "edit-text":
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
                node = editor.HtmlDoc.find_id(id)
                if node is None:
                    print("指定节点不存在")
                    continue
                else:
                    node.text = text
            case _:
                print("非法指令, 输入\"help\"查看帮助")
