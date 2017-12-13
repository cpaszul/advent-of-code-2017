DEFAULT_INPUT = 'day13.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        scanners = [list(map(int, line.strip().split(': '))) for line in f.readlines()]
    return sum(scan[0] * scan[1]
               for scan in scanners
               if scan[0] % ((scan[1] - 1) * 2) == 0)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        scanners = [list(map(int, line.strip().split(': '))) for line in f.readlines()]
    delay = 1
    while True:
        if all((scan[0] + delay) % ((scan[1] - 1) * 2) != 0
               for scan in scanners):
            return delay
        delay += 1

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
