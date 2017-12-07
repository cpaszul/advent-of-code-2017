DEFAULT_INPUT = 'day1.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        captcha = f.readline()
    captcha += captcha[0]
    return sum(int(a)
               for a, b in zip(captcha, captcha[1:])
               if a == b)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        captcha = f.readline()
    return sum(int(val)
               for ind, val in enumerate(captcha)
               if val == captcha[(ind + len(captcha)//2) % len(captcha)])

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
