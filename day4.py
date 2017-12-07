DEFAULT_INPUT = 'day4.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        phrases = [row.strip().split() for row in f.readlines()]
    return sum(1 for row in phrases if len(row) == len(set(row)))

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        phrases = [row.strip().split() for row in f.readlines()]
    return sum(1 for row in phrases if part_2_valid(row))

def part_2_valid(phrase):
    words = set()
    for word in phrase:
        new_word = ''.join(sorted(word))
        if new_word in words:
            return False
        words.add(new_word)
    return True

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
