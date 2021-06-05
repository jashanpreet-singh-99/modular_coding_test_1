import os
from tree import Tree

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

# Compare files


def compare_files():
    missing_files = []
    extra_files = []


directory_tree = Tree("root_node")
directory_tree.add_child(directory_tree.root, "node_L")
directory_tree.add_child(directory_tree.root, "node_M")
directory_tree.add_child(directory_tree.root, "node_R")
print(directory_tree)
