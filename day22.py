from collections import defaultdict

DEFAULT_INPUT = 'day22.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        rows = [line.strip() for line in f.readlines()]
    grid = defaultdict(lambda : '.')
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
    x = len(rows[0]) // 2
    y = len(rows) // 2
    # 0 = 'U', 1 = 'R', 2 = 'D', 3 = 'L'
    direction = 0
    infections = 0
    for _ in range(10000):
        if grid[(x, y)] == '#':
            direction = (direction + 1) % 4
            grid[(x, y)] = '.'
        else:
            direction = (direction - 1) % 4
            grid[(x, y)] = '#'
            infections += 1
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        else:
            x -= 1
    return infections

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        rows = [line.strip() for line in f.readlines()]
    grid = defaultdict(lambda : '.')
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
    x = len(rows[0]) // 2
    y = len(rows) // 2
    # 0 = 'U', 1 = 'R', 2 = 'D', 3 = 'L'
    direction = 0
    infections = 0
    for _ in range(10000000):
        if grid[(x, y)] == '#':
            direction = (direction + 1) % 4
            grid[(x, y)] = 'F'
        elif grid[(x, y)] == 'W':
            grid[(x, y)] = '#'
            infections += 1
        elif grid[(x, y)] == 'F':
            direction = (direction + 2) % 4
            grid[(x, y)] = '.'
        else:
            direction = (direction - 1) % 4
            grid[(x, y)] = 'W'
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        else:
            x -= 1
    return infections

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
