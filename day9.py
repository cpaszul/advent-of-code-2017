DEFAULT_INPUT = 'day9.txt'

def day_9(loc=DEFAULT_INPUT):
    with open(loc) as f:
        data = f.readline()
    i = 0
    group_score = 0
    score = 0
    in_garbage = False
    garbage_size = 0
    while i < len(data):
        char = data[i]
        if in_garbage:
            if char == '!':
                i += 1
            elif char == '>':
                in_garbage = False
            else:
                garbage_size += 1
        else:
            if char == '<':
                in_garbage = True
            elif char == '{':
                group_score += 1
            elif char == '}':
                score += group_score
                group_score -= 1
        i += 1
    return score, garbage_size

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_9()))
