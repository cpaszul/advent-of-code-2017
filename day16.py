DEFAULT_INPUT = 'day16.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        moves = f.readline().strip().split(',')
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    return ''.join(dance(programs, moves))

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        moves = f.readline().strip().split(',')
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    patterns = []
    for i in range(1000000000):
        if ''.join(programs) in patterns:
            return patterns[1000000000 % i]
        patterns.append(''.join(programs))
        programs = dance(programs, moves)

def dance(programs, moves):
    for move in moves:
        if move[0] == 's':
            rotate_amount = int(move[1:])
            programs = programs[-1 * rotate_amount:] + programs[:-1 * rotate_amount]
        elif move[0] == 'x':
            pos1, pos2 = map(int, move[1:].split('/'))
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        else:
            prog1, prog2 = move[1:].split('/')
            pos1 = programs.index(prog1)
            pos2 = programs.index(prog2)
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
