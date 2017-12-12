from collections import defaultdict

DEFAULT_INPUT = 'day12.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        connections = [line.strip() for line in f.readlines()]
    graph = defaultdict(set)
    for connect in connections:
        l, rs = connect.split(' <-> ')
        rs = rs.split(', ')
        for r in rs:
            graph[l].add(r)
            graph[r].add(l)
    seen = set()
    stack = ['0']
    while stack:
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            for connect in graph[current]:
                if connect not in seen:
                    stack.append(connect)
    return len(seen)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        connections = [line.strip() for line in f.readlines()]
    graph = defaultdict(set)
    for connect in connections:
        l, rs = connect.split(' <-> ')
        rs = rs.split(', ')
        for r in rs:
            graph[l].add(r)
            graph[r].add(l)
    seen = set()
    groups = 0
    keys = graph.keys()
    stack = []
    for key in keys:
        if key not in seen:
            stack.append(key)
            while stack:
                current = stack.pop()
                if current not in seen:
                    seen.add(current)
                    for connect in graph[current]:
                        if connect not in seen:
                            stack.append(connect)
            groups += 1
    return groups

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
