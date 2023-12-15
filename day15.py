from collections import defaultdict

DEFAULT_INPUT = 'day15.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        steps = list(f.readline().rstrip().split(','))
    return sum(algo(step) for step in steps)

def algo(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def part_2(loc: str = DEFAULT_INPUT) -> int:
    boxes = defaultdict(list)
    lenses = {}
    with open(loc) as f:
        steps = list(f.readline().rstrip().split(','))
    for step in steps:
        if '-' in step:
            label = step[:-1]
            box = algo(label)
            if label in boxes[box]:
                boxes[box].pop(boxes[box].index(label))
        else:
            label, lens = step.split('=')
            box = algo(label)
            if label not in boxes[box]:
                boxes[box].append(label)
            lenses[label] = int(lens)
    result = 0
    for box, labels in boxes.items():
        for i, label in enumerate(labels):
            result += (box + 1) * (i + 1) * lenses[label]
    return result

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
