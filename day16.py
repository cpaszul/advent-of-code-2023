from collections import deque

DEFAULT_INPUT = 'day16.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    return energize(grid, (0, 0, 1, 0))

def energize(grid: list[str], start: tuple[int, int, int, int]) -> int:
    max_y = len(grid)
    max_x = len(grid[0])
    seen = set()
    states = {start}
    d = deque([start])
    while d:
        x, y, dx, dy = d.pop()
        if 0 <= x < max_x and 0 <= y < max_y:
            tile = grid[y][x]
            seen.add((x, y))
            if tile == '.':
                new_position = (x + dx, y + dy, dx, dy)
                if new_position not in states:
                    states.add(new_position)
                    d.append(new_position)
            if tile == '\\':
                new_position = (x + dy, y + dx, dy, dx)
                if new_position not in states:
                    states.add(new_position)
                    d.append(new_position)
            if tile == '/':
                new_position = (x - dy, y - dx, -1 * dy, -1 * dx)
                if new_position not in states:
                    states.add(new_position)
                    d.append(new_position)
            if tile == '-':
                if (dx, dy) in ((0, 1), (0, -1)):
                    positions = [(x + 1, y, 1, 0), (x - 1, y, -1, 0)]
                    for new_position in positions:
                        if new_position not in states:
                            states.add(new_position)
                            d.append(new_position)
                else:
                    new_position = (x + dx, y + dy, dx, dy)
                    if new_position not in states:
                        states.add(new_position)
                        d.append(new_position)
            if tile == '|':
                if (dx, dy) in ((1, 0), (-1, 0)):
                    positions = [(x, y + 1, 0, 1), (x, y - 1, 0, -1)]
                    for new_position in positions:
                        if new_position not in states:
                            states.add(new_position)
                            d.append(new_position)
                else:
                    new_position = (x + dx, y + dy, dx, dy)
                    if new_position not in states:
                        states.add(new_position)
                        d.append(new_position)
    return len(seen)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    start_positions = []
    max_y = len(grid)
    max_x = len(grid[0])
    for x in range(max_x):
        start_positions.append((x, 0, 0, 1))
        start_positions.append((x, max_y - 1, 0, -1))
    for y in range(max_y):
        start_positions.append((0, y, 1, 0))
        start_positions.append((max_x - 1, y, -1, 0))
    return max(energize(grid, start_pos) for start_pos in start_positions)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
