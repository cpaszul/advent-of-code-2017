from collections import defaultdict

DEFAULT_INPUT = 'day24.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        comps = [tuple(map(int, line.strip().split('/'))) for line in f.readlines()]
    graph = defaultdict(set)
    for comp in comps:
        graph[comp[0]].add(comp)
        graph[comp[1]].add(comp)
    max_strength = 0
    def bridge_strength(bridge):
        return sum(a + b for a, b in bridge)
    stack = [([], 0)]
    while stack:
        bridge, port = stack.pop()
        max_strength = max(max_strength, bridge_strength(bridge))
        for comp in graph[port]:
            if comp not in bridge:
                new_bridge = bridge + [comp]
                if comp[0] == port:
                    stack.append((new_bridge, comp[1]))
                else:
                    stack.append((new_bridge, comp[0]))
    return max_strength


def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        comps = [tuple(map(int, line.strip().split('/'))) for line in f.readlines()]
    graph = defaultdict(set)
    for comp in comps:
        graph[comp[0]].add(comp)
        graph[comp[1]].add(comp)
    max_length = 0
    max_len_strength = 0
    def bridge_strength(bridge):
        return sum(a + b for a, b in bridge)
    stack = [([], 0)]
    while stack:
        bridge, port = stack.pop()
        bridge_len = len(bridge)
        if bridge_len > max_length:
            max_length = bridge_len
            max_len_strength = bridge_strength(bridge)
        elif bridge_len == max_length:
            max_len_strength = max(max_len_strength, bridge_strength(bridge))
        for comp in graph[port]:
            if comp not in bridge:
                new_bridge = bridge + [comp]
                if comp[0] == port:
                    stack.append((new_bridge, comp[1]))
                else:
                    stack.append((new_bridge, comp[0]))
    return max_len_strength

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
