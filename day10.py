from collections import defaultdict, deque

DEFAULT_INPUT = 'day10.txt'

type Point = tuple[int, int]

def day_10(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    grid = defaultdict(list)
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.rstrip()):
                if cell == 'S':
                    start = (x, y)
                grid[(x, y)] = cell
    path = get_path(grid, start)
    return len(path) // 2, find_interior(grid, path)

def get_path(grid: dict[Point, list[str]], start: Point) -> set[Point]:
    above = (start[0], start[1] - 1)
    below = (start[0], start[1] + 1)
    left = (start[0] - 1, start[1])
    right = (start[0] + 1, start[1])
    tile_dirs = {'|': [(0, 1), (0, -1)],
                 '-': [(1, 0), (-1, 0)],
                 'L': [(1, 0), (0, -1)],
                 'J': [(-1, 0), (0, -1)],
                 '7': [(-1, 0), (0, 1)],
                 'F': [(1, 0), (0, 1)],
                 '.': []}
    possibilities = []
    if (0, 1) in tile_dirs[grid[above]]:
        if (0, -1) in tile_dirs[grid[below]]:
            possibilities.append('|')
        if (1, 0) in tile_dirs[grid[left]]:
            possibilities.append('J')
        if (-1, 0) in tile_dirs[grid[right]]:
            possibilities.append('L')
    if (0, -1) in tile_dirs[grid[below]]:
        if (1, 0) in tile_dirs[grid[left]]:
            possibilities.append('7')
        if (-1, 0) in tile_dirs[grid[right]]:
            possibilities.append('F')
    if (1, 0) in tile_dirs[grid[left]] and (-1, 0) in tile_dirs[grid[right]]:
        possiblities.append('-')
    grid[start] = possibilities[0]
    d = deque([start])
    path = set([start])
    max_length = 0
    while d:
        current = d.popleft()
        x, y = current
        for dx, dy in tile_dirs[grid[current]]:
            if (x + dx, y + dy) not in path:
                path.add((x + dx, y + dy))
                d.append((x + dx, y + dy))
    return path

def find_interior(grid: dict[Point, list[tuple[int, int]]], path: set[Point]) -> int:
    max_x = max(grid.keys(), key=lambda p:p[0])[0]
    max_y = max(grid.keys(), key=lambda p:p[1])[1]
    start = (0, 0, 'left', 'upper')
    seen = set([start])
    d = deque([start])
    while d:
        x, y, x_half, y_half = d.popleft()
        adj = []
        if (x > 0 and x_half == 'left') or \
           (x_half == 'right' and y_half == 'upper' and ((x, y) not in path or grid[(x, y)] not in '|JL')) or \
           (x_half == 'right' and y_half == 'lower' and ((x, y) not in path or grid[(x, y)] not in '|7F')):
            adj.append('left')
        if (x < max_x and x_half == 'right') or \
           (x_half == 'left' and y_half == 'upper' and ((x, y) not in path or grid[(x, y)] not in '|JL')) or \
           (x_half == 'left' and y_half == 'lower' and ((x, y) not in path or grid[(x, y)] not in '|7F')):
            adj.append('right')
        if (y > 0 and y_half == 'upper') or \
           (x_half == 'right' and y_half == 'lower' and ((x, y) not in path or grid[(x, y)] not in '-LF')) or \
           (x_half == 'left' and y_half == 'lower' and ((x, y) not in path or grid[(x, y)] not in '-J7')):
            adj.append('up')
        if (y < max_y and y_half == 'lower') or \
           (x_half == 'right' and y_half == 'upper' and ((x, y) not in path or grid[(x, y)] not in '-LF')) or \
           (x_half == 'left' and y_half == 'upper' and ((x, y) not in path or grid[(x, y)] not in '-J7')):
            adj.append('down')
        if 'left' in adj:
            if x_half == 'left':
                new_position = (x - 1, y, 'right', y_half)
            else:
                new_position = (x, y, 'left', y_half)
            if new_position not in seen:
                seen.add(new_position)
                d.append(new_position)
        if 'right' in adj:
            if x_half == 'right':
                new_position = (x + 1, y, 'left', y_half)
            else:
                new_position = (x, y, 'right', y_half)
            if new_position not in seen:
                seen.add(new_position)
                d.append(new_position)
        if 'up' in adj:
            if y_half == 'upper':
                new_position = (x, y - 1, x_half, 'lower')
            else:
                new_position = (x, y, x_half, 'upper')
            if new_position not in seen:
                seen.add(new_position)
                d.append(new_position)
        if 'down' in adj:
            if y_half == 'lower':
                new_position = (x, y + 1, x_half, 'upper')
            else:
                new_position = (x, y, x_half, 'lower')
            if new_position not in seen:
                seen.add(new_position)
                d.append(new_position)
    total_tiles = set()
    for (x, y, x_half, y_half) in seen:
        if all(tile in seen for tile in ((x, y, 'left', 'upper'), (x, y, 'right', 'upper'),
                                         (x, y, 'left', 'lower'),(x, y, 'right', 'lower'))):
            total_tiles.add((x, y))
    return (max_x + 1) * (max_y + 1) - (len(total_tiles) + len(path))
    
if __name__ == '__main__':
    part_1, part_2 = day_10()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
