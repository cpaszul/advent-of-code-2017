DEFAULT_INPUT = 324

def part_1(steps=DEFAULT_INPUT):
    current_position = 0
    buffer = [0]
    for i in range(1, 2018):
        current_position = (current_position + steps) % len(buffer)
        buffer.insert(current_position + 1, i)
        current_position += 1
    return buffer[(current_position + 1) % len(buffer)]

def part_2(steps=DEFAULT_INPUT):
    current_position = 0
    pos_one = None
    for i in range(1, 50000001):
        current_position = (current_position + steps) % i
        if current_position == 0:
            pos_one = i
        current_position += 1
    return pos_one

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
