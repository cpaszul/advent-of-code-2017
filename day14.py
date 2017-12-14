from day10 import knot_hash

DEFAULT_INPUT = 'jxqlasbh'

def hash_to_bin(h):
    return ''.join(bin(int(c, 16))[2:].zfill(4) for c in h)

def day_14(puzzle_input=DEFAULT_INPUT):
    used = set()
    for y in range(128):
        row = hash_to_bin(knot_hash(puzzle_input + '-' + str(y)))
        for x, char in enumerate(row):
            if char == '1':
                used.add((x, y))
    seen = set()
    regions = 0
    stack = []
    for point in used:
        if point not in seen:
            seen.add(point)
            stack.append(point)
            while stack:
                current = stack.pop()
                x, y = current
                possible_neighbors = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < 128 and 0 <= y + j < 128 and \
                           xor(i == 0, j == 0):
                            possible_neighbors.append((x + i, y + j))
                for neigh in possible_neighbors:
                    if neigh in used and neigh not in seen:
                        stack.append(neigh)
                        seen.add(neigh)
            regions += 1
    return len(used), regions

def xor(a, b):
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_14()))
