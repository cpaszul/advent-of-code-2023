from collections import Counter
import re

DEFAULT_INPUT = 'day2.txt'

def day_2(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = f.readlines()
    pattern = re.compile(r'(\d+) (red|blue|green)')
    part_1_result = 0
    part_2_result = 0
    for line in lines:
        max_colors = Counter()
        for num, color in pattern.findall(line):
            max_colors[color] = max(max_colors[color], int(num))
        if max_colors['red'] <= 12 and max_colors['green'] <= 13 and max_colors['blue'] <= 14:
            part_1_result += int(line.split(': ')[0].split(' ')[1])
        part_2_result += max_colors['red'] * max_colors['green'] * max_colors['blue']
    return part_1_result, part_2_result

if __name__ == '__main__':
    part_1, part_2 = day_2()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
