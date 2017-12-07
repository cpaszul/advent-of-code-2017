DEFAULT_INPUT = 289326

class Spiral():
    def __init__(self, puzzle_input):
        self.spiral = {(0, 0): 1, (1, 0): 1}
        self.largest = 1
        self.direction = 'U'
        self.location = (1, 0)
        while self.largest < puzzle_input:
            self._gen_next_dir_and_loc()
            self._gen_location_value()
            self.largest = max(self.largest, self.spiral[self.location])

    def _gen_next_dir_and_loc(self):
        if self.direction == 'U' and \
           (self.location[0] - 1, self.location[1]) not in self.spiral:
            self.direction = 'L'
            self.location = (self.location[0] - 1, self.location[1])
        elif self.direction == 'U':
            self.location = (self.location[0], self.location[1] + 1)
        elif self.direction == 'L' and \
             (self.location[0], self.location[1] - 1) not in self.spiral:
            self.direction = 'D'
            self.location = (self.location[0], self.location[1] - 1)
        elif self.direction == 'L':
            self.location = (self.location[0] - 1, self.location[1])
        elif self.direction == 'D' and \
             (self.location[0] + 1, self.location[1]) not in self.spiral:
            self.direction = 'R'
            self.location = (self.location[0] + 1, self.location[1])
        elif self.direction == 'D':
            self.location = (self.location[0], self.location[1] - 1)
        elif self.direction == 'R' and \
             (self.location[0], self.location[1] + 1) not in self.spiral:
            self.direction = 'U'
            self.location = (self.location[0], self.location[1] + 1)
        else:
            self.location = (self.location[0] + 1, self.location[1])

    def _gen_location_value(self):
        adjacents = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i, j) != (0, 0):
                    adjacents.append((self.location[0] + i,
                                      self.location[1] + j))
        value = sum(self.spiral[adj_loc]
                    for adj_loc in adjacents
                    if adj_loc in self.spiral)
        self.spiral[self.location] = value

def part_1(puzzle_input=DEFAULT_INPUT):
    i = 3
    j = 1
    while i**2 < puzzle_input:
        i += 2
        j += 1
    bottom_right = i ** 2
    bottom_left = i ** 2 - (i - 1)
    top_left = i ** 2 - (i - 1) * 2
    top_right = i ** 2 - (i - 1) * 3
    min_val = (i - 2) ** 2 + 1
    if min_val <= puzzle_input <= top_right:
        center = (min_val - 1 + top_right) // 2
    elif top_right <= puzzle_input <= top_left:
        center = (top_right + top_left) // 2
    elif top_left <= puzzle_input <= bottom_left:
        center = (top_left + bottom_left) // 2
    else:
        center = (bottom_left + bottom_right) // 2
    return abs(center - puzzle_input) + j

def part_2(puzzle_input=DEFAULT_INPUT):
    spiral = Spiral(puzzle_input)
    return spiral.largest

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
