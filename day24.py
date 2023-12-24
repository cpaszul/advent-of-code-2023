from itertools import combinations
import re
from z3 import Int, Solver

DEFAULT_INPUT = 'day24.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            x, y, z, dx, dy, dz = map(int, re.findall(r'(-?\d+)', line))
            lines.append((x, y, dx, dy))
    result = 0
    min_pos = 200000000000000
    max_pos = 400000000000000
    for line_one, line_two in combinations(lines, 2):
        x1, y1, dx1, dy1 = line_one
        x2 = x1 + dx1
        y2 = y1 + dy1
        x3, y3, dx3, dy3 = line_two
        x4 = x3 + dx3
        y4 = y3 + dy3
        if ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)) == 0:
            continue
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        if min_pos <= px <= max_pos and min_pos <= py <= max_pos and \
           at_time(line_one, (px, py)) > 0 and at_time(line_two, (px, py)) > 0:
            result += 1
    return result

def at_time(line: tuple[int, int, int, int], point: tuple[float, float]) -> float:
    return (point[0] - line[0]) / line[2]
                
def part_2(loc: str = DEFAULT_INPUT) -> int:
    # I've never used z3 before
    # with help from old.reddit.com/r/adventofcode/comments/18pnycy/2023_day_24_solutions/keplyao/
    s = Solver()
    rx, ry, rz = Int('rx'), Int('ry'), Int('rz')
    rdx, rdy, rdz = Int('rdx'), Int('rdy'), Int('rdz')
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            x, y, z, dx, dy, dz = map(int, re.findall(r'(-?\d+)', line))
            lines.append((x, y, z, dx, dy, dz))
    for i, line in enumerate(lines[:3]):
        x, y, z, dx, dy, dz = line
        t = Int(f't{i}')
        s.add(t >= 0)
        s.add(x + dx * t == rx + rdx * t)
        s.add(y + dy * t == ry + rdy * t)
        s.add(z + dz * t == rz + rdz * t)
    assert str(s.check()) == 'sat'
    return s.model().eval(rx + ry + rz)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
