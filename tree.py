from node import Node


class Tree:
    def __init__(self, root=None):
        self.level_val = {}
        if isinstance(root, Node):
            self.root = root
        elif isinstance(root, str):
            self.root = Node(root)
        elif root is None:
            self.root = Node(None)
        else:
            message = f"Variable : root({type(root)}) -> is not of"\
                    " type Node."
            raise Node.NodeValueError(message)

    def update_tree(self):
        self.level_val = {}
        self.level_val[0] = [self.root.value]
        level_count = 1
        parent = self.root
        prev_parent = None
        child_count = 0
        while True:
            if len(parent.child) > 0:
                for child in parent.child:
                    if level_count not in self.level_val.keys():
                        self.level_val[level_count] = []
                    if not isinstance(child, Node):
                        message = f"Variable : child({type(child)}) of parent"\
                                f" : {parent.value} -> is not of type Node."
                        raise Node.NodeValueError(message)
                    self.level_val[level_count].append(child.value)
                if (len(self.level_val[level_count - 1]) - 1) == child_count:
                    prev_parent = parent
                    parent = parent.child[0]
                    level_count += 1
                    child_count = 0
                else:
                    break
            else:
                if (len(self.level_val[level_count - 1]) - 1) != child_count:
                    child_count += 1
                    parent = prev_parent.child[child_count]
                else:
                    break

    def __str__(self):
        self.update_tree()
        return_string = 'TREE : \n'
        for k, v in self.level_val.items():
            return_string += f' {k} : {self.level_val[k]}\n'
        return return_string

    def get_levels(self):
        self.update_tree()
        if len(self.level_val.keys()) > 0:
            return len(self.level_val.keys())
        else:
            return -1

    def get_child_count(self, level=0):
        if level != 0:
            return len(self.level_val[level])
        else:
            return 1

    def get_root(self):
        return self.root
