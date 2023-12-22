from collections import defaultdict, deque

DEFAULT_INPUT = 'day21.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    rocks = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                rocks.add((x, y))
            if cell == 'S':
                start = (x, y)
    max_y = len(grid)
    max_x = len(grid[0])
    seen = {start}
    d = deque([(*start, 0)])
    gardens = set()
    while d:
        x, y, steps = d.popleft()
        if steps % 2 == 0:
            gardens.add((x, y))
        if steps == 64:
            continue
        adjs = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        for adj_x, adj_y in adjs:
            if 0 <= adj_x < max_x and 0 <= adj_y <= max_y and \
               (adj_x, adj_y) not in seen and (adj_x, adj_y) not in rocks:
                d.append((adj_x, adj_y, steps + 1))
                seen.add((adj_x, adj_y))
    return len(gardens)
                
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    rocks = set()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                rocks.add((x, y))
            if cell == 'S':
                start = (x, y)
    max_y = len(grid)
    max_x = len(grid[0])
    gardens = defaultdict(set)
    gardens[0] = {start}
    i = 0
    results = []
    while True:
        for x, y in gardens[i]:
            adjs = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            for adj_x, adj_y in adjs:
                if (adj_x % 131, adj_y % 131) not in rocks:
                    gardens[i + 1].add((adj_x, adj_y))
        if i % 131 == 65:
            results.append(len(gardens[i]))
        if len(results) == 3:
            break
        i += 1
    # with help from old.reddit.com/r/adventofcode/comments/18nevo3/2023_day_21_solutions/keaihbm/
    b0 = results[0]
    b1 = results[1] - results[0]
    b2 = results[2] - results[1]
    f = lambda n: b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)
    desired = 26501365 // 131
    return f(desired)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
