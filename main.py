from src.parse import parse, print_tree
from src.converter import converter

posfile = open("postags.txt", "r")
depfile = open("dependency.txt", "r")

postags = []
dependencies = []

for line in posfile:
    if "/" not in line:
        break
    line = "".join(line.split())
    idx = line.index("/")
    pair = (line[:idx], line[idx+1:])
    postags += [pair]

for line in depfile:
    if "," not in line:
        break
    line = "".join(line.split())
    idx = 0
    while True:
        if line[idx] == "," and not (line[idx+1] == "-" and line[idx+2].isnumeric()):
            break
        idx += 1
    leftb = line.find("(")
    rightb = line.rfind(")")
    pair = (line[leftb+1:idx], line[idx+1:rightb])
    if "ROOT" in pair[0]:
        root = pair[1]
    else:
        dependencies += [pair]

# print(postags)
# print(dependencies)

tree = parse(postags, dependencies, root)
tree = converter(tree)
print_tree(tree)


# Example output: (VP (NP (NP (PRP$ My-1)(NN aunt-2)(POS 's-3))(MD can-4)(NN opener-5))(MD can-6)(VB open-7)(NP (DT a-8)(NN drum-9))(. .-10))