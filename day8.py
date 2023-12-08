import re
from math import lcm

DEFAULT_INPUT = 'day8.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    graph = {}
    with open(loc) as f:
        path, _, *nodes = (line.rstrip() for line in f.readlines())
    for node in nodes:
        start, left, right = re.findall(r'\w+', node)
        graph[start] = (left, right)
    current = 'AAA'
    i = 0
    n = 1
    while True:
        move = path[i]
        if move == 'R':
            current = graph[current][1]
        else:
            current = graph[current][0]
        if current == 'ZZZ':
            return n
        i += 1
        i %= len(path)
        n += 1

def part_2(loc: str = DEFAULT_INPUT) -> int:
    graph = {}
    with open(loc) as f:
        path, _, *nodes = (line.rstrip() for line in f.readlines())
    for node in nodes:
        start, left, right = re.findall(r'\w+', node)
        graph[start] = (left, right)
    all_starts = [node for node in graph.keys() if node[2] == 'A']
    cycle_lengths = []
    for current in all_starts:
        i = 0
        n = 1
        while True:
            move = path[i]
            if move == 'R':
                current = graph[current][1]
            else:
                current = graph[current][0]
            if current[2] == 'Z':
                cycle_lengths.append(n)
                break
            i += 1
            i %= len(path)
            n += 1
    return lcm(*cycle_lengths)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
