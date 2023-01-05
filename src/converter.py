from src.tree import Node


def transform(node):
    # move X down
    new_node = Node(node.get_token(), node.get_pos(), node.get_id())

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
    children = node.get_children()
    for i, child in enumerate(children):
        if len(child.get_children()) > 0:
            transform(child)

    # set a new projection XP
    children += [new_node]
    children.sort(key=lambda x: x.get_id())
    node.set_token("")
    node.set_children(children)
    node.set_id(max([child.get_id() for child in node.get_children()]))


def converter(tree):
    transform(tree.get_root())
    return tree


