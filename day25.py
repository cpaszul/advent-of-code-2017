from collections import defaultdict, namedtuple
import re

DEFAULT_INPUT = 'day25.txt'

State = namedtuple('State', ['zero_write', 'zero_move', 'zero_state',
                             'one_write', 'one_move', 'one_state'])

def day_25(loc=DEFAULT_INPUT):
    with open(loc) as f:
        current_state = f.readline().split(' ')[-1][0]
        step_count = int(f.readline().split(' ')[-2])
        raw_instructions = ''.join(f.readlines())
    pattern = re.compile(r'In state (\w):\s+' +
                         r'If the current value is 0:\s+' +
                         r'- Write the value (\d).\s+' +
                         r'- Move one slot to the (\w+).\s+' +
                         r'- Continue with state (\w).\s+' +
                         r'If the current value is 1:\s+' +
                         r'- Write the value (\d).\s+' +
                         r'- Move one slot to the (\w+).\s+' +
                         r'- Continue with state (\w).')
    tape = defaultdict(int)
    states = {}
    cursor = 0
    for instruction in pattern.finditer(raw_instructions):
        s = instruction[1]
        inst = State(int(instruction[2]), 1 if instruction[3] == 'right' else -1, instruction[4],
                     int(instruction[5]), 1 if instruction[6] == 'right' else -1, instruction[7])
        states[s] = inst
    for _ in range(step_count):
        instructions = states[current_state]
        if tape[cursor] == 0:
            tape[cursor] = instructions.zero_write
            cursor += instructions.zero_move
            current_state = instructions.zero_state
        else:
            tape[cursor] = instructions.one_write
            cursor += instructions.one_move
            current_state = instructions.one_state
    return sum(tape.values())

if __name__ == '__main__':
    print('Solution for Part One:', day_25())
