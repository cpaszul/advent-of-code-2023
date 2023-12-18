from collections import deque

DEFAULT_INPUT = 'day18.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    walls = {(0, 0)}
    with open(loc) as f:
        lines = [line.rstrip().split(' ') for line in f.readlines()]
    x = 0
    y = 0
    for line in lines:
        direct, n, c = line
        n = int(n)
        for _ in range(n):
            if direct == 'L':
                x -= 1
            if direct == 'R':
                x += 1
            if direct == 'U':
                y -= 1
            if direct == 'D':
                y += 1
            walls.add((x, y))
    left = min(walls, key=lambda p:p[0])[0]
    left_wall = {y for (x, y) in walls if x == left}
    top = min(left_wall)
    start = (left + 1, top + 1)
    interior = {start}
    d = deque([start])
    while d:
        current_x, current_y = d.popleft()
        adjs = [(current_x + 1, current_y), (current_x - 1, current_y),
                (current_x, current_y + 1), (current_x, current_y - 1)]
        for adj in adjs:
            if adj not in interior and adj not in walls:
                interior.add(adj)
                d.append(adj)
    return len(interior) + len(walls)


def draw(walls):
    min_x = min(walls, key=lambda p:p[0])[0]
    min_y = min(walls, key=lambda p:p[1])[1]
    max_x = max(walls, key=lambda p:p[0])[0]
    max_y = max(walls, key=lambda p:p[1])[1]
    rows = []
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in walls:
                row += '#'
            else:
                row += '.'
        rows.append(row)
    print('\n'.join(rows))

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    points = [(0, 0)]
    x = 0
    y = 0
    perimeter = 0
    for line in lines:
        h = line[-7:-1]
        dist = int(h[:-1], 16)
        perimeter += dist
        direct = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[h[-1]]
        if direct == 'L':
            x -= dist
        if direct == 'R':
            x += dist
        if direct == 'U':
            y -= dist
        if direct == 'D':
            y += dist
        points.append((x, y))
    area = 0
    for point_one, point_two in zip(points, points[1:]):
        x_a, y_a = point_one
        x_b, y_b = point_two
        area += (x_a * y_b) - (x_b * y_a)
    return perimeter // 2 + area // 2 + 1

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
