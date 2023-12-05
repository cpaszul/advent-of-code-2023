from string import digits

DEFAULT_INPUT = 'day1.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        return sum([int((line_ints := [char for char in line if char in digits])[0] + line_ints[-1])
                    for line in f.readlines()])

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        return sum(to_int(line) for line in f.readlines())

def to_int(line: str) -> int:
    line = line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e') \
           .replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x') \
           .replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e')
    line_ints = [char for char in line if char in digits]
    return int(line_ints[0] + line_ints[-1])

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
