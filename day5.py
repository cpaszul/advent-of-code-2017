DEFAULT_INPUT = 'day5.txt'

def day_5(part_two, loc=DEFAULT_INPUT):
    with open(loc) as f:
        jumps = [int(line.strip()) for line in f.readlines()]
    steps = 0
    i = 0
    while i >= 0:
        # try/except is noticably faster than checking i < len(jumps)
        try:
            lines_to_move = jumps[i]
        except IndexError:
            return steps
        if part_two and jumps[i] >= 3:
            jumps[i] -= 1
        else:
            jumps[i] += 1
        i += lines_to_move
        steps += 1
    return steps

if __name__ == '__main__':
    print('Solution for Part One:', day_5(False))
    print('Solution for Part Two:', day_5(True))
