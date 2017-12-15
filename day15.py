DEFAULT_INPUT = 'day15.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        gen_a = int(f.readline().split(' ')[-1])
        gen_b = int(f.readline().split(' ')[-1])
    matching = 0
    for _ in range(40000000):
        gen_a *= 16807
        gen_a %= 2147483647
        gen_b *= 48271
        gen_b %= 2147483647
        if bin(gen_a)[-16:] == bin(gen_b)[-16:]:
            matching += 1
    return matching

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        a = int(f.readline().split(' ')[-1])
        b = int(f.readline().split(' ')[-1])
    gen_a = gen(a, 16807, 4)
    gen_b = gen(b, 48271, 8)
    matching = 0
    for _ in range(5000000):
        val_a = next(gen_a)
        val_b = next(gen_b)
        if bin(val_a)[-16:] == bin(val_b)[-16:]:
            matching += 1
    return matching

def gen(value, multiplier, multiple):
    while True:
        value *= multiplier
        value %= 2147483647
        if value % multiple == 0:
            yield value

if __name__ == '__main__':
    #print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
