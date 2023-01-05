from src.tree import Node, Tree


def parse(postags, dependencies):
    dic = {}
    for postag in postags:
        node = Node(postag[0], postag[1])
        dic[postag[0]] = node

    findroot = set(dic.keys())

    for parent, child in dependencies:
        if child not in dic[parent].get_children():
            children = dic[parent].get_children()
            children += [dic[child]]
            dic[parent].set_children(children)
        findroot.remove(child)

    root = dic[list(findroot)[0]]
    tree = Tree(root)

    return tree


def traverse_children(node, out):
    for child in node.get_children():
        out += "(" + child.get_pos() + " "
        if len(child.get_token()) > 0:
            out += child.get_token()
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
