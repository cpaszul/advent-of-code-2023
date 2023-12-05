DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = [line.rstrip().split(': ')[1].split(' | ') for line in f.readlines()]
    part_1_result = 0
    copies = [1] * len(lines)
    for i, line in enumerate(lines):
        left, right = line
        left_set = set(map(int, (num for num in left.split(' ') if num)))
        right_set = set(map(int, (num for num in right.split(' ') if num)))
        overlap = len(left_set & right_set)
        if overlap:
            part_1_result += 2 ** (overlap - 1)
            for n in range(1, overlap + 1):
                copies[i + n] += copies[i]
    return part_1_result, sum(copies)

if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
