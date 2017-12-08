from collections import defaultdict

DEFAULT_INPUT = 'day8.txt'

def day_8(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = [line.strip() for line in f.readlines()]
    registers = defaultdict(int)
    largest_value = 0
    operations = {'>': lambda a, b: a > b,
                  '>=': lambda a, b: a >= b,
                  '<': lambda a, b: a < b,
                  '<=': lambda a, b: a <= b,
                  '==': lambda a, b: a == b,
                  '!=': lambda a, b: a != b}
    for inst in instructions:
        reg, op, size, _, cond_reg, cond, cond_size = inst.split()
        size = int(size)
        cond_size = int(cond_size)
        if operations[cond](registers[cond_reg], cond_size):
            if op == 'inc':
                registers[reg] += size
            else:
                registers[reg] -= size
            largest_value = max(largest_value, registers[reg])
    register_values = list(registers.values())
    register_values.sort()
    return register_values[-1], largest_value

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_8()))
