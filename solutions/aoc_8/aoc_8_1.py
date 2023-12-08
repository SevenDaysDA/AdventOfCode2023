
strategy_line = ""
nodes = {}

with open('solutions/aoc_8/input_doc.txt', 'r') as file:
    lines = file.readlines()
    strategy_line = lines[0].strip() if len(lines) > 0 else ""

    for line in lines[2:]:
        line = line.strip()
        if '=' in line:
            node, options = line.split('=')
            node = node.strip()
            options = options.strip()[1:-1].split(',')
            options = tuple(opt.strip() for opt in options)
            nodes[node] = options

print("Strategy Line:", strategy_line)
print("Nodes and Options:")
print(nodes)
# for node, options in nodes.items():
#     print(f"{node}: {options}")


def direction_to_index(direction):
    print(direction)
    if direction == "L":
        return 0
    else:
        return 1



print()

epochs = 0
print(epochs)

index = 0

n = "AAA"
next_node = ""

while True:
    character = strategy_line[index]

    direction_index = direction_to_index(character)

    print(n)
    # import ipdb;ipdb.set_trace()
    n = nodes[n][direction_index]
    # print(node)

    index += 1

    if index == len(strategy_line):
        index = 0
        epochs += 1
        print(epochs)

    if n == "ZZZ":
        break

print(epochs)
print(index)

print(epochs*len(strategy_line)+index)
# print(nodes)