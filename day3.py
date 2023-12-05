from string import digits

DEFAULT_INPUT = 'day3.txt'

def day_3(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    numbers = []
    desired_numbers = set()
    gears = []
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            num = ''
            num_coords = []
            for x, cell in enumerate(line.rstrip()):
                if cell == '*':
                    gears.append((x, y))
                if cell in digits:
                    num += cell
                    num_coords.append((x, y))
                else:
                    if num != '':
                        numbers.append((int(num), num_coords))
                        num = ''
                        num_coords = []
                    if cell != '.':
                        desired_numbers |= {(x + i, y + j)
                                            for i in range(-1, 2)
                                            for j in range(-1, 2)}                        
            if num != '':
                numbers.append((int(num), num_coords))
    part_2_result = 0
    for x, y in gears:
        adj = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]
        adj_numbers = []
        for num, num_coords in numbers:
            if any(coord in adj for coord in num_coords):
                adj_numbers.append(num)
        if len(adj_numbers) == 2:
            part_2_result += adj_numbers[0] * adj_numbers[1]
    return sum(num[0] for num in numbers if
               any(coord in desired_numbers for coord in num[1])), \
           part_2_result

if __name__ == '__main__':
    part_1, part_2 = day_3()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
