
class Node:
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos
        self.children = []

    def get_token(self):
        return self.token

    def get_pos(self):
        return self.pos

    def get_children(self):
        return self.children

    def set_token(self, new_token):
        self.token = new_token

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_children(self, new_children):
        self.children = new_children


class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def set_root(self, new_root):
        self.root = new_root




