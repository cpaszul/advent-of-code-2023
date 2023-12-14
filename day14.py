DEFAULT_INPUT = 'day14.txt'

type Point = tuple[int, int]

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                grid[(x, y)] = cell
    max_y = max(grid, key=lambda p:p[1])[1]
    grid = move_rocks(grid, 0, -1)
    return sum(max_y + 1 - k[1] for k, v in grid.items() if v == 'O')

def move_rocks(grid: dict[Point, str], dx: int, dy: int) -> dict[Point, str]:
    while True:
        new_grid = {}
        for x, y in grid:
            if grid[(x, y)] == 'O' and (x + dx, y + dy) in grid and grid[(x + dx, y + dy)] == '.':
                new_grid[(x, y)] = '.'
                new_grid[(x + dx, y + dy)] = 'O'
            else:
                if (x, y) not in new_grid:
                    new_grid[(x, y)] = grid[(x, y)]
        if new_grid == grid:
            grid = new_grid
            break
        grid = new_grid
    return grid

def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                grid[(x, y)] = cell
    max_y = max(grid, key=lambda p:p[1])[1]
    states = {}
    i = 0
    state = frozenset(k for k, v in grid.items() if v == 'O')
    states[state] = i
    target = 1000000000
    while True:
        grid = move_rocks(grid, 0, -1)
        grid = move_rocks(grid, -1, 0)
        grid = move_rocks(grid, 0, 1)
        grid = move_rocks(grid, 1, 0)
        i += 1
        state = frozenset(k for k, v in grid.items() if v == 'O')
        if state not in states:
            states[state] = i
        else:
            cycle_length = i - states[state]
            desired = (target - states[state]) % cycle_length + states[state]
            break
    for state, time in states.items():
        if time == desired:
            return sum(max_y + 1 - y for _, y in state)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
