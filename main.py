import os
from tree import Tree
from node import Node

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

root_node = Node("root_value")
left_node = Node("left_value")
right_node = Node("right_value")

leaf_node_left = Node("Extreme left node.")
leaf_node_l_right = Node("Extreme left_left node.")
leaf_node_r_right = Node("Extreme left_right node.")

leaf_node_left.add_child(leaf_node_l_right)
leaf_node_left.add_child(leaf_node_r_right)


right_node.add_child(leaf_node_left)

root_node.add_child(left_node)
root_node.add_child(right_node)

t = Tree(root_node)
print(t)


def print_files(path, node):
    for files in os.listdir(path):
        file_node = Node(files)
        file_node = node.add_child(file_node)
        new_path = os.path.join(path, files)
        if os.path.isdir(new_path):
            if files[0] == '.':
                continue
            print_files(new_path, file_node)


# print_files(PATH_SRC)

directory_tree = Tree("SRC")
print_files(PATH_SRC, directory_tree.root)
print(directory_tree)
