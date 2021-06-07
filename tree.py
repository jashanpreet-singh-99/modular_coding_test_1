class Tree:
    def __init__(self, root):
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
                    level_val[level_count].append(child.value)
                parent = parent.child[0]
            else:
                break
        return_string = 'TREE : \n'
        for k, v in level_val.items():
            return_string += f' {k} : {level_val[k]}\n'
        return return_string
