from src.tree import Node


def transform(node):
    children = node.get_children()

    # set new projection of X
    new_node = Node(node.get_token(), node.get_pos())
    node.set_token("")

    # set XP
    pos = node.get_pos()
    if pos[0] == "N" or pos in ["CD"]:
        new_pos = "NP"
    elif node.get_pos()[0] == "V":
        new_pos = "VP"
    else:
        new_pos = "PP"
    node.set_pos(new_pos)

    # recursively convert its children
    for i, child in enumerate(children):
        if len(child.get_children()) == 0:
            new_children = children[:i+1] + [new_node] + children[i+1:]
            node.set_children(new_children)
        elif len(child.get_children()) > 0 and i == 0:
            new_children = [new_node] + children
            node.set_children(new_children)
            transform(child)
        else:
            transform(child)


def converter(tree):
    transform(tree.get_root())
    return tree


