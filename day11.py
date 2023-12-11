from itertools import combinations

DEFAULT_INPUT = 'day11.txt'

def day_11(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        grid = [line.rstrip() for line in f.readlines()]
    rows_to_expand = []
    cols_to_expand = []
    for y in range(len(grid)):
        if all(char == '.' for char in grid[y]):
            rows_to_expand.append(y)
    for x in range(len(grid[0])):
        if all(row[x] == '.' for row in grid):
            cols_to_expand.append(x)
    galaxies = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                galaxies.append((x, y))
    distances_p1 = 0
    distances_p2 = 0
    for gal_a, gal_b in combinations(galaxies, 2):
        x_a, y_a = gal_a
        x_b, y_b = gal_b
        expansions = []
        for x in range(min(x_a, x_b), max(x_a, x_b) + 1):
            if x in cols_to_expand:
                expansions.append(x)
        for y in range(min(y_a, y_b), max(y_a, y_b) + 1):
            if y in rows_to_expand:
                expansions.append(y)
        distances_p1 += abs(x_a - x_b) + abs(y_a - y_b) + len(expansions)
        distances_p2 += abs(x_a - x_b) + abs(y_a - y_b) + (999_999 * len(expansions))
    return distances_p1, distances_p2

if __name__ == '__main__':
    part_1, part_2 = day_11()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
