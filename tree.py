from node import Node


class Tree:
    def __init__(self, root=None):
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

    def __str__(self):
        level_val = {}
        level_val[0] = [self.root.value]
        level_count = 1
        parent = self.root
        prev_parent = None
        child_count = 0
        while True:
            if len(parent.child) > 0:
                for child in parent.child:
                    if level_count not in level_val.keys():
                        level_val[level_count] = []
                    if not isinstance(child, Node):
                        message = f"Variable : child({type(child)}) of parent"\
                                f" : {parent.value} -> is not of type Node."
                        raise Node.NodeValueError(message)
                    level_val[level_count].append(child.value)
                if (len(level_val[level_count - 1]) - 1) == child_count:
                    prev_parent = parent
                    parent = parent.child[0]
                    level_count += 1
                    child_count = 0
                else:
                    break

            else:
                if (len(level_val[level_count - 1]) - 1) != child_count:
                    child_count += 1
                    parent = prev_parent.child[child_count]
                else:
                    break
        return_string = 'TREE : \n'
        for k, v in level_val.items():
            return_string += f' {k} : {level_val[k]}\n'
        return return_string

    def get_root(self):
        return self.root
