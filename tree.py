from node import Node


class Tree:
    def __init__(self, root):
        if not isinstance(root, Node):
            message = f"Variable : root({type(root)}) -> is not of"\
                    " type Node."
            raise Node.NodeValueError(message)
        self.root = root

    def __str__(self):
        level_val = {}
        level_val[0] = self.root.value
        level_count = 1
        parent = self.root
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
                parent = parent.child[0]
                level_count += 1
            else:
                break
        return_string = 'TREE : \n'
        for k, v in level_val.items():
            return_string += f' {k} : {level_val[k]}\n'
        return return_string
