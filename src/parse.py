from src.tree import Node, Tree


def parse(postags, dependencies, root):
    dic = {}
    for i, postag in enumerate(postags):
        token = postag[0] + "-" + str(i+1)
        node = Node(token, postag[1], i+1)
        dic[token] = node

    for parent, child in dependencies:
        if child not in dic[parent].get_children():
            children = dic[parent].get_children()
            children += [dic[child]]
            dic[parent].set_children(children)

    tree = Tree(dic[root])

    return tree


def traverse_children(node, out):
    for child in node.get_children():
        out += "(" + child.get_pos() + " "
        token = child.get_token()
        if len(token) > 0:
            if token[0] == "(":
                out += "\\"
            out += token
        else:
            out = traverse_children(child, out)
        out += ")"
    return out


def print_tree(tree):
    root = tree.get_root()
    out = "(" + root.get_pos() + " "
    out = traverse_children(tree.get_root(), out)
    out += ")"
    print(out)
