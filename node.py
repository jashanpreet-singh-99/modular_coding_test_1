class Node:
    def __init__(self, value):
        self.value = value
        self.root = None
        self.child = []

    def set_root(self, root):
        self.root = root

    def set_value(self, value):
        self.value = value

    def add_child(self, child):
        child.set_root(self)
        self.child.append(child)

    def update_child(self, index, child):
        self.child[index] = child

    def replace_child(self, old_child, new_child):
        index = self.child.index(old_child)
        self.update_child(index, new_child)
