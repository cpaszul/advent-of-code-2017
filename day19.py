from string import ascii_uppercase

DEFAULT_INPUT = 'day19.txt'

def day_19(loc=DEFAULT_INPUT):
    with open(loc) as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    current_point = (grid[0].index('|'), 0)
    letters = ''
    can_move = True
    direction = 'D'
    steps = 0
    def valid_space(x, y):
        return 0 <= x < len(grid[0]) and \
               0 <= y < len(grid) and \
               grid[y][x] != ' '
    def get_next_move_and_dir():
        if direction == 'D':
            if valid_space(current_point[0], current_point[1] + 1):
                return (current_point[0], current_point[1] + 1), 'D'
            elif valid_space(current_point[0] + 1, current_point[1]):
                return (current_point[0] + 1, current_point[1]), 'R'
            elif valid_space(current_point[0] - 1, current_point[1]):
                return (current_point[0] - 1, current_point[1]), 'L'
            else:
                return None, None
        elif direction == 'U':
            if valid_space(current_point[0], current_point[1] - 1):
                return (current_point[0], current_point[1] - 1), 'U'
            elif valid_space(current_point[0] + 1, current_point[1]):
                return (current_point[0] + 1, current_point[1]), 'R'
            elif valid_space(current_point[0] - 1, current_point[1]):
                return (current_point[0] - 1, current_point[1]), 'L'
            else:
                return None, None
        elif direction == 'R':
            if valid_space(current_point[0] + 1, current_point[1]):
                return (current_point[0] + 1, current_point[1]), 'R'
            elif valid_space(current_point[0], current_point[1] + 1):
                return (current_point[0], current_point[1] + 1), 'D'
            elif valid_space(current_point[0], current_point[1] - 1):
                return (current_point[0], current_point[1] - 1), 'U'
            else:
                return None, None
        else:
            if valid_space(current_point[0] - 1, current_point[1]):
                return (current_point[0] - 1, current_point[1]), 'L'
            elif valid_space(current_point[0], current_point[1] + 1):
                return (current_point[0], current_point[1] + 1), 'D'
            elif valid_space(current_point[0], current_point[1] - 1):
                return (current_point[0], current_point[1] - 1), 'U'
            else:
                return None, None
    while can_move:
        current_point, direction = get_next_move_and_dir()
        steps += 1
        if not current_point:
            can_move = False
        else:
            if grid[current_point[1]][current_point[0]] in ascii_uppercase:
                letters += (grid[current_point[1]][current_point[0]])
    return letters, steps

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_19()))
