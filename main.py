import os
from tree import Tree
from node import Node

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")


def print_files(path, parent_node):
    for files in os.listdir(path):
        new_path = os.path.join(path, files)
        file_node = Node(files)
        file_node = parent_node.add_child(file_node)
        print(files, os.path.isdir(new_path))
        if os.path.isdir(new_path):
            if files[0] != '.':
                print_files(new_path, file_node)


# print_files(PATH_SRC)

# directory_tree = Tree("SRC")
# print_files(PATH_SRC, directory_tree.root)
# print(directory_tree)
# print("Levels : ", directory_tree.get_levels())


child_count = 0


def test_tree(tree_node):
    global child_count
    child = Node("child " + str(child_count))
    child_count += 1
    child = tree_node.add_child(child)
    if child_count != 5 and (child_count % 2) != 0:
        test_tree(child)
    elif (child_count % 2) == 0 and child_count != 5:
        test_tree(tree_node)


struct_tree = Tree("src")
test_tree(struct_tree.root)
print(struct_tree)
