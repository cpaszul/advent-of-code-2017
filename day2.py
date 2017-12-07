DEFAULT_INPUT = 'day2.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        rows = [line.strip().split() for line in f.readlines()]
    rows = [[int(num) for num in row]
            for row in rows]
    return sum(max(row) - min(row)
               for row in rows)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        rows = [line.strip().split() for line in f.readlines()]
    rows = [[int(num) for num in row]
            for row in rows]
    return sum(find_even_divide(row) for row in rows)

def find_even_divide(row):
    for i_ind in range(len(row)):
        for j_ind in range(i_ind + 1, len(row)):
            if row[i_ind] % row[j_ind] == 0:
                return row[i_ind] // row[j_ind]
            elif row[j_ind] % row[i_ind] == 0:
                return row[j_ind] // row[i_ind]
    return 0

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
