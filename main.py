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
