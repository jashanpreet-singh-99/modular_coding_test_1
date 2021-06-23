import os
from tree import Tree
from node import Node

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

root = Node("src")


def path_to_tree(path, node):
    if os.path.isdir(path):
        dir_list = os.listdir(path)
        for dir in dir_list:
            child_node = Node(dir)
            node.add_child(child_node)
            if dir[0] == '.':
                continue
            child_path = os.path.join(path, dir)
            if os.path.isdir(child_path):
                path_to_tree(child_path, child_node)
            else:
                print(dir)


path_to_tree(PATH_SRC, root)
print(Tree(root))
