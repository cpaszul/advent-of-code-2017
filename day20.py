from collections import defaultdict

DEFAULT_INPUT = 'day20.txt'

class Particle():
    def __init__(self, particle_id, p, v, a):
        self.px, self.py, self.pz = map(int, p.rstrip('>').lstrip('p=<').split(','))
        self.vx, self.vy, self.vz = map(int, v.rstrip('>').lstrip('v=<').split(','))
        self.ax, self.ay, self.az = map(int, a.rstrip('>').lstrip('a=<').split(','))
        self.id = particle_id
        self.base_p = self.px, self.py, self.pz
        self.base_v = self.vx, self.vy, self.vz
        self.base_a = self.ax, self.ay, self.az

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    @property
    def distance(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

    @property
    def p(self):
        return self.px, self.py, self.pz
        
def part_1(cycles, loc=DEFAULT_INPUT):
    with open(loc) as f:
        particles = [Particle(index, *line.strip().split(', ')) for index, line in enumerate(f.readlines())]
    for particle in particles:
        for _ in range(cycles):
            particle.update()
    distances = [(p.id, p.distance) for p in particles]
    distances.sort(key=lambda p:p[1])
    return distances[0][0]

def part_2(cycles, loc=DEFAULT_INPUT):
    with open(loc) as f:
        particles = [Particle(index, *line.strip().split(', ')) for index, line in enumerate(f.readlines())]
    for _ in range(cycles):
        positions = defaultdict(list)
        for particle in particles:
            particle.update()
            positions[particle.p].append(particle.id)
        particles_to_delete = []
        for val in positions.values():
            if len(list(val)) > 1:
                particles_to_delete += list(val)
        particles = [particle for particle in particles if particle.id not in particles_to_delete]
    return len(particles)

if __name__ == '__main__':
    print('Solution for Part One:', part_1(10000))
    print('Solution for Part Two:', part_2(10000))
