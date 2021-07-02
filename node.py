from exceptions import NodeValueError


class Node:
    def __init__(self, value, char_limit=0):
        self.value = value
        self.root = None
        self.child = []
        self.char_limit = char_limit

    def __str__(self):
        if self.char_limit > 0:
            if len(self.value) > self.char_limit:
                return '[ ' + self.value[:self.char_limit] + '.. ]'
        return '[ ' + self.value + ' ]'

    def set_root(self, root):
        if not isinstance(root, Node):
            message = f"Variable : root({type(root)}) -> is not of"\
                    " type Node."
            raise NodeValueError(message)
        self.root = root

    def set_value(self, value):
        self.value = value

    def add_child(self, child):
        if not isinstance(child, Node):
            message = f"Variable : child({type(child)}) -> is not of"\
                    " type Node."
            raise NodeValueError(message)
        child.set_root(self)
        self.child.append(child)
        return child

    def update_child(self, index, child):
        if not isinstance(child, Node):
            message = f"Variable : child({type(child)}) -> is not of\
             type Node."
            raise NodeValueError(message)
        self.child[index] = child

    def replace_child(self, old_child, new_child):
        if not isinstance(old_child, Node):
            message = f"Variable : old_child({type(old_child)}) -> is not of"\
                    " type Node."
            raise NodeValueError(message)
        elif not isinstance(new_child, Node):
            message = f"Variable : new_child({type(new_child)}) -> is not of"\
                    " type Node."
            raise NodeValueError(message)
        index = self.child.index(old_child)
        self.update_child(index, new_child)
