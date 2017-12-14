from functools import reduce

DEFAULT_INPUT = 'day10.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        input_list = [int(n) for n in f.readline().split(',')]
    number_list = list(range(256))
    current_pos = 0
    skip_size = 0
    for num in input_list:
        offset = current_pos - 0
        number_list = rotate(number_list, offset)
        section = number_list[0:num]
        section.reverse()
        number_list[0:num] = section
        number_list = rotate(number_list, -1 * offset)
        current_pos += (num + skip_size)
        current_pos %= len(number_list)
        skip_size += 1
    return number_list[0] * number_list[1]

def rotate(lst, n):
    return lst[n:] + lst[:n]

def knot_hash(input_str):
    str_as_bytes = [ord(char) for char in input_str]
    str_as_bytes += [17, 31, 73, 47, 23]
    number_list = list(range(256))
    current_pos = 0
    skip_size = 0
    for _ in range(64):
        for num in str_as_bytes:
            offset = current_pos - 0
            number_list = rotate(number_list, offset)
            section = number_list[0:num]
            section.reverse()
            number_list[0:num] = section
            number_list = rotate(number_list, -1 * offset)
            current_pos += (num + skip_size)
            current_pos %= len(number_list)
            skip_size += 1
    dense_hash = [reduce(lambda a, b: a ^ b, number_list[i:i+16])
                  for i in range(0, 256, 16)]
    return ''.join(hex(num)[2:].zfill(2) for num in dense_hash)

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        return knot_hash(f.readline())

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
