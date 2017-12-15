DEFAULT_INPUT = 'day15.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        a = int(f.readline().split(' ')[-1])
        b = int(f.readline().split(' ')[-1])
    gen_a = gen(a, 16807)
    gen_b = gen(b, 48271)
    return sum((next(gen_a) & 0xffff) == (next(gen_b) & 0xffff)
               for _ in range(40000000))

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        a = int(f.readline().split(' ')[-1])
        b = int(f.readline().split(' ')[-1])
    gen_a = gen(a, 16807, 4)
    gen_b = gen(b, 48271, 8)
    return sum((next(gen_a) & 0xffff) == (next(gen_b) & 0xffff)
               for _ in range(5000000))

def gen(value, multiplier, multiple=1):
    while True:
        value *= multiplier
        value %= 2147483647
        if value % multiple == 0:
            yield value

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
