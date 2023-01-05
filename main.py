from src.parse import parse, print_tree
from src.converter import converter

posfile = open("postags.txt", "r")
depfile = open("dependency.txt", "r")

postags = []
dependencies = []

for line in posfile:
    if ":" not in line:
        break
    line = "".join(line.split())
    idx = line.index(":")
    pair = (line[:idx], line[idx+1:])
    postags += [pair]

for line in depfile:
    if "," not in line:
        break
    line = "".join(line.split())
    idx = line.index(",")
    pair = (line[:idx], line[idx+1:])
    dependencies += [pair]

tree = parse(postags, dependencies)
tree = converter(tree)
print_tree(tree)
