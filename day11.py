from collections import defaultdict

DEFAULT_INPUT = 'day11.txt'

def day_11(loc=DEFAULT_INPUT):
    with open(loc) as f:
        moves = f.readline().strip().split(',')
    move_dict = defaultdict(int)
    furthest_distance = 0
    for move in moves:
        if move == 'n':
            if move_dict['s']:
                move_dict['s'] -= 1
            elif move_dict['se']:
                move_dict['se'] -= 1
                move_dict['ne'] += 1
            elif move_dict['sw']:
                move_dict['sw'] -= 1
                move_dict['nw'] += 1
            else:
                move_dict['n'] += 1
        elif move == 'ne':
            if move_dict['sw']:
                move_dict['sw'] -= 1
            elif move_dict['s']:
                move_dict['s'] -= 1
                move_dict['se'] += 1
            elif move_dict['nw']:
                move_dict['nw'] -= 1
                move_dict['n'] += 1
            else:
                move_dict['ne'] += 1
        elif move == 'nw':
            if move_dict['se']:
                move_dict['se'] -= 1
            elif move_dict['s']:
                move_dict['s'] -= 1
                move_dict['sw'] += 1
            elif move_dict['ne']:
                move_dict['ne'] -= 1
                move_dict['n'] += 1
            else:
                move_dict['nw'] += 1
        elif move == 's':
            if move_dict['n']:
                move_dict['n'] -= 1
            elif move_dict['ne']:
                move_dict['ne'] -= 1
                move_dict['se'] += 1
            elif move_dict['nw']:
                move_dict['nw'] -= 1
                move_dict['sw'] += 1
            else:
                move_dict['s'] += 1
        elif move == 'se':
            if move_dict['nw']:
                move_dict['nw'] -= 1
            elif move_dict['n']:
                move_dict['n'] -= 1
                move_dict['ne'] += 1
            elif move_dict['sw']:
                move_dict['sw'] -= 1
                move_dict['s'] += 1
            else:
                move_dict['se'] += 1
        else: # move == 'sw'
            if move_dict['ne']:
                move_dict['ne'] -= 1
            elif move_dict['n']:
                move_dict['n'] -= 1
                move_dict['nw'] += 1
            elif move_dict['se']:
                move_dict['se'] -= 1
                move_dict['s'] += 1
            else:
                move_dict['sw'] += 1
        furthest_distance = max(furthest_distance, sum(move_dict.values()))
    return sum(move_dict.values()), furthest_distance

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_11()))
