import re

DEFAULT_INPUT = 'day6.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        times = list(map(int, re.findall(r'\d+', f.readline())))
        distances = list(map(int, re.findall(r'\d+', f.readline())))
    result = 1
    for t, d in zip(times, distances):
        victories = 0
        for charge_time in range(1, t):
            if charge_time * (t - charge_time) > d:
                victories += 1
        result *= victories
    return result

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        t = int(''.join(re.findall(r'\d', f.readline())))
        d = int(''.join(re.findall(r'\d', f.readline())))
    for charge_time in range(1, t):
        if charge_time * (t - charge_time) > d:
            lower = charge_time
            break
    for charge_time in range(t, 0, -1):
        if charge_time * (t - charge_time) > d:
            upper = charge_time
            break
    return upper - lower + 1

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
