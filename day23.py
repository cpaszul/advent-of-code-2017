from collections import defaultdict
from string import ascii_lowercase

DEFAULT_INPUT = 'day23.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = [line.strip() for line in f.readlines()]
    regs = defaultdict(int)
    muls = 0
    i = 0
    def get_value(n):
        if n in ascii_lowercase:
            return regs[n]
        else:
            return int(n)
    while 0 <= i < len(instructions):
        inst = instructions[i]
        op, x, y = inst.split(' ')
        if op == 'set':
            regs[x] = get_value(y)
        elif op == 'sub':
            regs[x] -= get_value(y)
        elif op == 'mul':
            regs[x] *= get_value(y)
            muls += 1
        else:
            if get_value(x) != 0:
                i += get_value(y) - 1
        i += 1
    return muls

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        _, _, base_value = f.readline().strip().split(' ')
    base_value = int(base_value)
    h = 0
    start = base_value * 100 + 100000
    for i in range(start, start + 17001, 17):
        for n in range(2, i):
            if i % n == 0:
                h += 1
                break
    return h

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
