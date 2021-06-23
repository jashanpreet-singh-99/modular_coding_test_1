import os
from tree import Tree
from node import Node

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

struct_tree = Tree("src")


def path_to_tree(path, tree, level, child):
    if os.path.isdir(path):
        dir_list = os.listdir(path)
        for dir in dir_list:
            pass


path_to_tree(PATH_SRC, struct_tree, struct_tree.get_levels(),
             struct_tree.get_child_count())
