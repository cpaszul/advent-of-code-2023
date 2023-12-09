DEFAULT_INPUT = 'day9.txt'

def day_9(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = [list(map(int, line.split(' '))) for line in f.readlines()]
    return sum(get_next_value(line) for line in lines), \
           sum(get_prev_value(line) for line in lines)

def get_next_value(history: list[int]) -> int:
    histories = [history]
    while True:
        hist = histories[-1]
        if all(ele == 0 for ele in hist):
            break
        next_history = []
        for val_1, val_2 in zip(hist, hist[1:]):
            next_history.append(val_2 - val_1)
        histories.append(next_history)
    for n in range(len(histories) - 1, 0, -1):
        histories[n - 1].append(histories[n - 1][-1] + histories[n][-1])
    return histories[0][-1]

def get_prev_value(history: list[int]) -> int:
    histories = [history]
    while True:
        hist = histories[-1]
        if all(ele == 0 for ele in hist):
            break
        next_history = []
        for val_1, val_2 in zip(hist, hist[1:]):
            next_history.append(val_2 - val_1)
        histories.append(next_history)
    for n in range(len(histories) - 1, 0, -1):
        histories[n - 1] = [histories[n - 1][0] - histories[n][0]] + histories[n - 1]
    return histories[0][0]

if __name__ == '__main__':
    part_1, part_2 = day_9()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
