from functools import reduce

DEFAULT_INPUT = 'day10.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        input_list = [int(n) for n in f.readline().split(',')]
    number_list = list(range(256))
    number_list, _, _ = knot_hash(number_list, input_list, 0, 0)
    return number_list[0] * number_list[1]

def rotate(lst, n):
    return lst[n:] + lst[:n]

def knot_hash(number_list, input_list, current_position, skip_size):
    for input_num in input_list:
        offset = current_position - 0
        number_list = rotate(number_list, offset)
        section = number_list[0:input_num]
        section.reverse()
        number_list[0:input_num] = section
        number_list = rotate(number_list, -1 * offset)
        current_position += (input_num + skip_size)
        current_position %= len(number_list)
        skip_size += 1
    return number_list, current_position, skip_size

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        input_list = [ord(char) for char in f.readline()]
    input_list += [17, 31, 73, 47, 23]
    number_list = list(range(256))
    current_position = 0
    skip_size = 0
    for _ in range(64):
        number_list, current_position, skip_size = \
                     knot_hash(number_list, input_list, current_position, skip_size)
    dense_hash = []
    for i in range(0, 256, 16):
        dense_hash.append(reduce(lambda a, b: a ^ b, number_list[i:i+16]))
    output = ''.join(hex(num)[2:].zfill(2) for num in dense_hash)
    return output

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
