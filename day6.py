DEFAULT_INPUT = 'day6.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        blocks = [int(num) for num in f.readline().split()]
    seen = set()
    steps = 0
    while tuple(blocks) not in seen:
        seen.add(tuple(blocks))
        steps += 1
        index_highest = blocks.index(max(blocks))
        highest = blocks[index_highest]
        blocks[index_highest] = 0
        i = index_highest + 1
        for _ in range(highest):
            if i >= len(blocks):
                i = 0
            blocks[i] += 1
            i += 1
    return steps

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        blocks = [int(num) for num in f.readline().split()]
    states = {}
    step = 0
    while True:
        t_blocks = tuple(blocks)
        if t_blocks in states:
            return step - states[t_blocks]
        else:
            states[t_blocks] = step
        index_highest = blocks.index(max(blocks))
        highest = blocks[index_highest]
        blocks[index_highest] = 0
        i = index_highest + 1
        for _ in range(highest):
            if i >= len(blocks):
                i = 0
            blocks[i] += 1
            i += 1
        step += 1

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
