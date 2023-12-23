from collections import defaultdict, deque

DEFAULT_INPUT = 'day23.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.rstrip()):
                grid[(x, y)] = cell
                if cell == '.' and y == 0:
                    start = (x, y)
    max_y = max(grid.keys(), key=lambda p:p[1])[1]
    goal = [key for key in grid if key[1] == max_y and grid[key] == '.'][0]
    longest_path = 0
    d = deque([(start, {start})])
    while d:
        current, path = d.popleft()
        if current == goal:
            longest_path = max(longest_path, len(path) - 1)
            continue
        x, y = current
        tile = grid[current]
        if tile == '.':
            adjs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if tile == '>':
            adjs = [(x + 1, y)]
        if tile == '<':
            adjs = [(x - 1, y)]
        if tile == 'v':
            adjs = [(x, y + 1)]
        if tile == '^':
            adjs = [(x, y - 1)]
        for adj in adjs:
            if adj in grid and grid[adj] != '#' and adj not in path:
                d.append((adj, path | {adj}))
    return longest_path
                
def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.rstrip()):
                grid[(x, y)] = cell if cell == '#' else '.'
                if cell == '.' and y == 0:
                    start = (x, y)
    max_y = max(grid.keys(), key=lambda p:p[1])[1]
    goal = [key for key in grid if key[1] == max_y and grid[key] == '.'][0]
    nodes = {start, goal}
    for x, y in grid:
        if sum((adj in grid and grid[adj] == '.') for adj in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))) > 2:
            nodes.add((x, y))
    graph = defaultdict(dict)
    for node in nodes:
        d = deque([(node, 0)])
        seen = {node}
        while d:
            current, path_len = d.popleft()
            if current != node and current in nodes:
                graph[node][current] = path_len
                continue
            x, y = current
            adjs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for adj in adjs:
                if adj in grid and grid[adj] != '#' and adj not in seen:
                    seen.add(adj)
                    d.append((adj, path_len + 1))
    longest_path = 0
    d = deque([(start, {start}, 0)])
    while d:
        current, path, path_len = d.popleft()
        if current == goal:
            longest_path = max(longest_path, path_len)
            continue
        connections = graph[current]
        for node, distance in connections.items():
            if node not in path:
                d.append((node, path | {node}, path_len + distance))
    return longest_path

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
