class Tree:
    def __init__(self, root):
        self.root = root
        self.children = {}

    def __str__(self):
        return f'Root -> {self.root}'

    def add_child(self, parent, child):
        if self.root not in self.children.keys() or \
                len(self.children[parent]) == 0:
            self.children[parent] = [child]
        else:
            self.children[parent].append(child)
