from collections import defaultdict
from string import ascii_lowercase

DEFAULT_INPUT = 'day18.txt'

def part_1(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = [line.strip() for line in f.readlines()]
    regs = defaultdict(int)
    i = 0
    last_sound = None
    def get_value(x):
        if x in ascii_lowercase:
            return regs[x]
        else:
            return int(x)
    while 0 <= i < len(instructions):
        spl = instructions[i].split()
        inst = spl[0]
        if inst == 'snd':
            last_sound = get_value(spl[1])
            i += 1
        elif inst == 'set':
            regs[spl[1]] = get_value(spl[2])
            i += 1
        elif inst == 'add':
            regs[spl[1]] += get_value(spl[2])
            i += 1
        elif inst == 'mul':
            regs[spl[1]] *= get_value(spl[2])
            i += 1
        elif inst == 'mod':
            regs[spl[1]] %= get_value(spl[2])
            i += 1
        elif inst == 'rcv':
            if get_value(spl[1]) != 0:
                return last_sound
            else:
                i += 1
        else:
            if get_value(spl[1]) > 0:
                i += get_value(spl[2])
            else:
                i += 1
    return None

def part_2(loc=DEFAULT_INPUT):
    with open(loc) as f:
        instructions = [line.strip() for line in f.readlines()]
    regs_0, regs_1 = defaultdict(int), defaultdict(int)
    regs_0['p'] = 0
    regs_1['p'] = 1
    can_act_0, can_act_1 = True, True
    queue_0, queue_1 = [], []
    i_0, i_1 = 0, 0
    prog_1_send = 0
    def get_value(x, prog):
        if x not in ascii_lowercase:
            return int(x)
        elif prog == 0:
            return regs_0[x]
        else:
            return regs_1[x]
    while can_act_0 or can_act_1:
        #Program 0 acts:
        if can_act_0 and 0 <= i_0 < len(instructions):
            spl = instructions[i_0].split()
            inst = spl[0]
            if inst == 'snd':
                val = get_value(spl[1], 0)
                queue_1.append(val)
                can_act_1 = True
                i_0 += 1
            elif inst == 'set':
                regs_0[spl[1]] = get_value(spl[2], 0)
                i_0 += 1
            elif inst == 'add':
                regs_0[spl[1]] += get_value(spl[2], 0)
                i_0 += 1
            elif inst == 'mul':
                regs_0[spl[1]] *= get_value(spl[2], 0)
                i_0 += 1
            elif inst == 'mod':
                regs_0[spl[1]] %= get_value(spl[2], 0)
                i_0 += 1
            elif inst == 'rcv':
                if queue_0:
                    val = queue_0.pop(0)
                    regs_0[spl[1]] = val
                    i_0 += 1
                else:
                    can_act_0 = False
            else:
                if get_value(spl[1], 0) > 0:
                    i_0 += get_value(spl[2], 0)
                else:
                    i_0 += 1
        else:
            can_act_0 = False
        #Program 1 acts:
        if can_act_1 and 0 <= i_1 < len(instructions):
            spl = instructions[i_1].split()
            inst = spl[0]
            if inst == 'snd':
                val = get_value(spl[1], 1)
                queue_0.append(val)
                can_act_0 = True
                i_1 += 1
                prog_1_send += 1
            elif inst == 'set':
                regs_1[spl[1]] = get_value(spl[2], 1)
                i_1 += 1
            elif inst == 'add':
                regs_1[spl[1]] += get_value(spl[2], 1)
                i_1 += 1
            elif inst == 'mul':
                regs_1[spl[1]] *= get_value(spl[2], 1)
                i_1 += 1
            elif inst == 'mod':
                regs_1[spl[1]] %= get_value(spl[2], 1)
                i_1 += 1
            elif inst == 'rcv':
                if queue_1:
                    val = queue_1.pop(0)
                    regs_1[spl[1]] = val
                    i_1 += 1
                else:
                    can_act_1 = False
            else:
                if get_value(spl[1], 1) > 0:
                    i_1 += get_value(spl[2], 1)
                else:
                    i_1 += 1
        else:
            can_act_1 = False
    return prog_1_send

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
