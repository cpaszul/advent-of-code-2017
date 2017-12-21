DEFAULT_INPUT = 'day21.txt'

class TransformationDict:
    def __init__(self, rules):
        self.patterns = {}
        for rule in rules:
            start, result = rule.split(' => ')
            start_r = self.rotate(start)
            start_rr = self.rotate(start_r)
            start_rrr = self.rotate(start_rr)
            start_f = self.flip(start)
            start_fr = self.rotate(start_f)
            start_frr = self.rotate(start_fr)
            start_frrr = self.rotate(start_frr)
            for pattern in [start, start_r, start_rr, start_rrr,
                            start_f, start_fr, start_frr, start_frrr]:
                self.patterns[pattern] = result

    def rotate(self, pattern_string):
        pattern = string_to_pattern(pattern_string)
        return pattern_to_string(list(zip(*pattern[::-1])))

    def flip(self, pattern_string):
        pattern = string_to_pattern(pattern_string)
        return pattern_to_string(row[::-1] for row in pattern)

    def transform(self, pattern):
        return string_to_pattern(self.patterns[pattern_to_string(pattern)])

def pattern_to_string(pattern):
    return '/'.join(''.join(row) for row in pattern)

def string_to_pattern(pattern_string):
    return list(row for row in pattern_string.split('/'))
        
def day_21(iterations, loc=DEFAULT_INPUT):
    with open(loc) as f:
        trans_dict = TransformationDict(line.strip() for line in f.readlines())
    current = ['.#.', '..#', '###']
    for _ in range(iterations):
        if len(current) in (2, 3):
            current = trans_dict.transform(current)
        else:
            split_pattern = split(current)
            transformed_pattern = []
            for row in split_pattern:
                transformed_row = []
                for block in row:
                    transformed_block = trans_dict.transform(block)
                    transformed_row.append(transformed_block)
                transformed_pattern.append(transformed_row)
            current = join(transformed_pattern)
    return sum(char == '#' for char in pattern_to_string(current))

def split(pattern):
    rows = []
    y = 0
    size = len(pattern)
    inner_size = 2 if size % 2 == 0 else 3
    while y < size:
        x = 0
        row = []
        while x < size:
            block = []
            for i_y in range(y, y + inner_size):
                block_row = ''
                for i_x in range(x, x + inner_size):
                    block_row += pattern[i_y][i_x]
                block.append(block_row)
            row.append(block)
            x += inner_size
        rows.append(row)
        y += inner_size
    return rows

def join(pattern_matrix):
    pattern = []
    block_size = len(pattern_matrix[0][0])
    for row in pattern_matrix:
        for y in range(block_size):
            pattern_row = ''
            for block in row:
                pattern_row += block[y]
            pattern.append(pattern_row)
    return pattern

'''
def join(patterns):
    total_size = len(patterns)
    size = int(math.sqrt(total_size))
    rows = []
    for i in range(0, total_size, size):
        section = patterns[i:i+size]
        section = [section_row.split('/') for section_row in section]
        for j in range(size):
            row = ''
            for subsection in section:
                row += subsection[j]
            rows.append(row)
    return '/'.join(rows)
'''
               
def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        pass
    return None

if __name__ == '__main__':
    print('Solution for Part One:', day_21(5))
    print('Solution for Part Two:', day_21(18))
                
