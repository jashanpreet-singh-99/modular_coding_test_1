import os
from tree import Tree
from node import Node

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

root_node = Node("root_value")
left_node = Node("left_value")
right_node = Node("right_value")

leaf_node = Node("Extreme node.")

left_node.add_child(leaf_node)

root_node.add_child(left_node)
root_node.add_child(right_node)

t = Tree(root_node)
print(t)
