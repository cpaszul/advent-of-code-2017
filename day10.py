from functools import reduce

DEFAULT_INPUT = 'day10.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        input_list = [int(n) for n in f.readline().split(',')]
    curr_list = list(range(256))
    curr_pos = 0
    skip_size = 0
    for inp in input_list:
        offset = curr_pos - 0
        curr_list = rotate(curr_list, offset)
        section = curr_list[0:inp]
        section.reverse()
        curr_list[0:inp] = section
        curr_list = rotate(curr_list, -1 * offset)
        curr_pos += (inp + skip_size)
        curr_pos %= len(curr_list)
        skip_size += 1
    return curr_list[0] * curr_list[1]

def rotate(lst, n):
    return lst[n:] + lst[:n]

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        input_list = [ord(char) for char in f.readline()]
    input_list += [17, 31, 73, 47, 23]
    curr_list = list(range(256))
    curr_pos = 0
    skip_size = 0
    for _ in range(64):
        for inp in input_list:
            offset = curr_pos - 0
            curr_list = rotate(curr_list, offset)
            section = curr_list[0:inp]
            section.reverse()
            curr_list[0:inp] = section
            curr_list = rotate(curr_list, -1 * offset)
            curr_pos += (inp + skip_size)
            curr_pos %= len(curr_list)
            skip_size += 1
    dense_hash = []
    for i in range(0, 256, 16):
        dense_hash.append(reduce(lambda a, b: a ^ b, curr_list[i:i+16]))
    output = ''.join(hex(num)[2:].zfill(2) for num in dense_hash)
    return output

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
