from collections import defaultdict

DEFAULT_INPUT = 'day7.txt'

class ProgramTree():
    def __init__(self, name, tree):
        self.name = name
        self.weight = tree[name][1]
        self.child_names = tree[name][2]
        self.children = {child: ProgramTree(child, tree)
                         for child in tree[name][2]}
        self.total_weight = self.weight + \
                            sum(child.total_weight
                                for child in self.children.values())

    #Assumption is exactly one program has an incorrect weight,
    # that no program has exactly one child, and that the root
    # program has at least three children
    def find_incorrect_weight(self):
        child_weights = {child.name: child.total_weight
                         for child in self.children.values()}
        child_weights = list(child_weights.items())
        child_weights.sort(key=lambda c:c[1])
        a, b, c = child_weights[0][1], child_weights[1][1], \
                  child_weights[-1][1]
        deviation = c - a
        if a == b:
            incorrect_path = child_weights[-1][0]
        else:
            incorrect_path = child_weights[0][0]
        return self.children[incorrect_path].find_incorrect_weight_recur(deviation)
    
    def find_incorrect_weight_recur(self, deviation):
        if not self.children:
            return self.weight - deviation
        child_weights = {child.name: child.total_weight
                         for child in self.children.values()}
        child_weights = list(child_weights.items())
        if all(child_weight[1] == child_weights[0][1]
               for child_weight in child_weights):
            return self.weight - deviation
        child_weights.sort(key=lambda c:c[1])
        if deviation < 0:
            incorrect_path = child_weights[0][0]
        else:
            incorrect_path = child_weights[-1][0]
        return self.children[incorrect_path].find_incorrect_weight_recur(deviation)


def day_7(loc=DEFAULT_INPUT):
    with open(loc) as f:
        programs = [line.strip() for line in f.readlines()]
    #dict format == {name: [parent, weight, [children]]}
    program_dict = defaultdict(lambda:[None, 0, []])
    for program in programs:
        program_split = program.split()
        if len(program_split) > 2:
            name = program_split[0]
            weight = int(program_split[1].rstrip(')').lstrip('('))
            children = program_split[3:]
            children = [child.rstrip(',') for child in children]
            program_dict[name][1] = weight
            program_dict[name][2] = children
            for child in children:
                program_dict[child][0] = name
        else:
            name = program_split[0]
            weight = int(program_split[1].rstrip(')').lstrip('('))
            program_dict[name][1] = weight
    for key, value in program_dict.items():
        if value[0] is None:
            parent = key
    pt = ProgramTree(parent, program_dict)
    return parent, pt.find_incorrect_weight()

if __name__ == '__main__':
    print('Solution for Part One: {}\nSolution for Part Two: {}'.format(*day_7()))
