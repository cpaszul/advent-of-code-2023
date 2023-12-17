import heapq

type Point = tuple[int, int]

DEFAULT_INPUT = 'day17.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [list(map(int, list(line.rstrip()))) for line in f.readlines()]
    max_y = len(grid)
    max_x = len(grid[0])
    seen = set()
    start = (0, 0, 0, 0, 0)
    h = [start]
    while h:
        heat, x, y, px, py = heapq.heappop(h)
        state = (x, y, px, py)
        if state in seen:
            continue
        seen.add(state)
        if (x, y) == (max_x - 1, max_y - 1):
            return heat
        for neigh in neighbors(grid, (x, y), (px, py)):
            node, cost = neigh
            heapq.heappush(h, (heat + cost, *node, x, y))

def neighbors(grid: list[list[int]], node: Point, prev: Point) -> list[tuple[Point, int]]:
    x, y = node
    px, py = prev
    max_y = len(grid)
    max_x = len(grid[0])
    neighs = []
    if x == px:
        for i in range(1, 4):
            if 0 <= x + i < max_x:
                cost = sum(grid[y][x + k] for k in range(1, i + 1))
                neighs.append(((x + i, y), cost))
        for i in range(-1, -4, -1):
            if 0 <= x + i < max_x:
                cost = sum(grid[y][x + k] for k in range(-1, i - 1, -1))
                neighs.append(((x + i, y), cost))
    if y == py:
        for i in range(1, 4):
            if 0 <= y + i < max_y:
                cost = sum(grid[y + k][x] for k in range(1, i + 1))
                neighs.append(((x, y + i), cost))
        for i in range(-1, -4, -1):
            if 0 <= y + i < max_y:
                cost = sum(grid[y + k][x] for k in range(-1, i - 1, -1))
                neighs.append(((x, y + i), cost))
    return neighs   

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [list(map(int, list(line.rstrip()))) for line in f.readlines()]
    max_y = len(grid)
    max_x = len(grid[0])
    seen = set()
    start = (0, 0, 0, 0, 0)
    h = [start]
    while h:
        heat, x, y, px, py = heapq.heappop(h)
        state = (x, y, px, py)
        if state in seen:
            continue
        seen.add(state)
        if (x, y) == (max_x - 1, max_y - 1):
            return heat
        for neigh in neighbors_p2(grid, (x, y), (px, py)):
            node, cost = neigh
            heapq.heappush(h, (heat + cost, *node, x, y))

def neighbors_p2(grid: list[list[int]], node: Point, prev: Point) -> list[tuple[Point, int]]:
    x, y = node
    px, py = prev
    max_y = len(grid)
    max_x = len(grid[0])
    neighs = []
    if x == px:
        for i in range(4, 11):
            if 0 <= x + i < max_x:
                cost = sum(grid[y][x + k] for k in range(1, i + 1))
                neighs.append(((x + i, y), cost))
        for i in range(-4, -11, -1):
            if 0 <= x + i < max_x:
                cost = sum(grid[y][x + k] for k in range(-1, i - 1, -1))
                neighs.append(((x + i, y), cost))
    if y == py:
        for i in range(4, 11):
            if 0 <= y + i < max_y:
                cost = sum(grid[y + k][x] for k in range(1, i + 1))
                neighs.append(((x, y + i), cost))
        for i in range(-4, -11, -1):
            if 0 <= y + i < max_y:
                cost = sum(grid[y + k][x] for k in range(-1, i - 1, -1))
                neighs.append(((x, y + i), cost))
    return neighs   

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
