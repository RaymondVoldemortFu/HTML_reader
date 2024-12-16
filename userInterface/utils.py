def welcome():
    print('-' * 40)
    print("欢迎使用HTML编辑器,输入 \"help\" 查看可用命令")
    print('-' * 40)


def print_help():
    print(
"""read path: 从指定路径读取 HTML 文件并解析为设计的数据结构
save path: 将当前 HTML 数据结构保存为指定路径的 HTML 文件
find-id id: 查找指定 id 的元素，输出元素的基本信息
find-tag tag: 查找所有标签名为 tag 的元素，输出所有匹配元素的信息。
insert tag id beforeId [text]: 在某节点之前插入新节点。tag 和 id 为新元素的标签和 ID，注意 ID 不能重复。
    beforeId 为插入位置的元素 ID，新元素将插入到该元素之前。[text] 为可选参数，表示新元素中的文本内容。
append tag id parentId [text]: 在某节点内插入新节点。parentId 为目标父元素的 ID。[text] 为可选参数，表示新元素中的文本内容。
delete id: 删除某元素。例如，delete last-updated。
edit-id oldId newId: 修改指定节点的 ID 为 newId。
edit-text id [text]: 修改指定节点的文本内容。
print-indent [n]: indent 为可选参数，表示每级缩进的空格数，默认为 2。当提供 indent 时，使用指定的空格数进行缩进显示。
print-tree: 按树型结构打印 HTML 对象。
undo: 撤销上一步操作。
redo: 重做上一次撤销的操作。
help: 显示支持的指令列表与用法。
exit: 退出编辑器。
        """
    )

