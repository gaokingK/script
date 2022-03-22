import json

# 应该把数据结构和构建区分开, 数据结构不需要实现从字典树到树的构建
# 另外 不应该建立Node类, 而且Tree类也不应该从Node类继承


# class Node:
#     def __init__(self, name, parent):
#         self.name = name
#         self.parent = parent
#         self.child = []
#     # 有监控方法吗?
#
#     def find_child(self):
#         self.child = dict_tree.get(self.name)

"""
To: 树的数据结构
二叉树怎么表示? 怎么画出树的数据结构
Python 实现树结构: 
    - https://blog.csdn.net/m0_37324740/article/details/79435814
    - https://blog.csdn.net/ailinyingai/article/details/102744193
如何画出一棵树: https://www.zhihu.com/question/280404022 
"""
class Tree:
    def __init__(self, root_name):
        self.root_name = root_name
        self.child = []
        self.node_num = 1

    def insert_node(self, node_name):
        self.child.append(Tree(node_name))
        self.node_num += 1

    def __str__(self):
        return self.root_name


"""
To: 使用字典表示的树, 输入某个节点, 给出当前节点所在树的节点树 
"""
def split_tree():
    """
    从字典树中挑出不同树的根结点
    :return: 根结点name 的列表
    """
    node_list = dict_tree.keys()
    child_node_list = list()
    [child_node_list.extend(x) for x in dict_tree.values()]
    root_node_list = []
    for node in node_list:
        status = False if node in child_node_list else True
        if status:
            root_node_list.append(node)
    return root_node_list


def init_tree(node_name, parent_tree):
    """
    传入树的根结点,在字典树中寻找是否有子节点, 有就添加
    :param node_name: 当前节点
    :param parent_tree: 当前节点父节点 type-> Tree
    :return: 递归方法
    """
    parent_tree.insert_node(node_name)
    # while dict_tree.get(node_name): # while 后不要跟不会变的变量,会死循环
    if dict_tree.get(node_name):
        # 防止父节点被多次初始化
        parent_tree = Tree(node_name)
        for child in dict_tree.get(node_name):
            init_tree(child, parent_tree)


def dict2tree(origin_str):
    global dict_tree
    dict_tree = json.loads(origin_str)

    root_node_list = split_tree()
    tree_chain = []

    for root in root_node_list:
        current_tree = Tree(root)
        tree_chain.append(current_tree)
        for child in dict_tree.get(root):
            init_tree(child, current_tree)


if __name__ == '__main__':
    tree_str = '{"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "H": ["I", "J"], "I": ["K", "L"]}'
    dict_tree = dict()
    dict2tree(tree_str)
