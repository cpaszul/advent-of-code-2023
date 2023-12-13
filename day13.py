DEFAULT_INPUT = 'day13.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        patterns = [pattern.split('\n') for pattern in f.read().split('\n\n')]
    result = 0
    for pattern in patterns:
        if vertical_reflection_line(pattern, True) != -1:
            result += vertical_reflection_line(pattern, True) + 1
        else:
            result += 100 * (horizontal_reflection_line(pattern, True) + 1)
    return result

def vertical_reflection_line(pattern: list[str], part_one: bool) -> int:
    for n in range(len(pattern[0]) - 1):
        differences = has_vert_reflect(pattern, n)
        if (part_one and differences == 0) or (not part_one and differences == 1):
            return n
    return -1

def has_vert_reflect(pattern: list[str], n: int) -> bool:
    differences = 0
    for i in range(1, len(pattern[0]) - n):
        if (n + 1 - i) >= 0:
            differences += diffs(col(pattern, n + 1 - i), col(pattern, n + i))
    return differences

def col(pattern: list[str], n: int) -> str:
    return ''.join(pattern[i][n] for i in range(len(pattern)))

def horizontal_reflection_line(pattern: list[str], part_one: bool) -> int:
    for n in range(len(pattern) - 1):
        differences = has_horiz_reflect(pattern, n)
        if (part_one and differences == 0) or (not part_one and differences == 1):
            return n
    return -1

def has_horiz_reflect(pattern: list[str], n: int) -> bool:
    differences = 0
    for i in range(1, len(pattern) - n):
        if (n + 1 - i) >= 0:
            differences += diffs(pattern[n + 1 - i], pattern[n + i])
    return differences

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        patterns = [pattern.split('\n') for pattern in f.read().split('\n\n')]
    result = 0
    for pattern in patterns:
        if vertical_reflection_line(pattern, False) != -1:
            result += vertical_reflection_line(pattern, False) + 1
        else:
            result += 100 * (horizontal_reflection_line(pattern, False) + 1)
    return result

def diffs(line_a: str, line_b: str) -> int:
    return sum(line_a[i] != line_b[i] for i in range(len(line_a)))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
