DEFAULT_INPUT = 324

def part_1(steps=DEFAULT_INPUT):
    current_position = 0
    buffer = [0]
    for i in range(1, 2018):
        current_position += steps
        current_position %= len(buffer)
        buffer.insert(current_position + 1, i)
        current_position += 1
        current_position %= len(buffer)
    return buffer[current_position + 1]

def part_2(steps=DEFAULT_INPUT):
    current_position = 0
    pos_one = None
    len_buffer = 1
    for i in range(1, 50000001):
        current_position += steps
        current_position %= len_buffer
        if current_position == 0:
            pos_one = i
        len_buffer += 1
        current_position += 1
        current_position %= len_buffer
    return pos_one

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
