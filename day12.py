from functools import cache

DEFAULT_INPUT = 'day12.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            row, nums_str = line.rstrip().split(' ')
            row = tuple(section for section in row.split('.') if section)
            nums = tuple(map(int, nums_str.split(',')))
            lines.append((row, nums))
    return sum(get_variations(*line) for line in lines)

@cache
def get_variations(blocks: tuple[str], nums: tuple[int]) -> int:
    if len(blocks) == 1:
        return block_variations(blocks[0], nums)
    return sum(block_variations(blocks[0], nums[:i]) * get_variations(blocks[1:], nums[i:])
               for i in range(len(nums) + 1))

@cache
def block_variations(block: str, nums: tuple[int]) -> int:
    gaps = max(len(nums) - 1, 0)
    if (sum(nums) > len(block)) or \
       (block.count('#') > sum(nums)) or \
       (block.count('?') < gaps) or \
       (sum(nums) + gaps > len(block)):
        return 0
    if block.count('#') == sum(nums) and block.count('?') == 0:
        return 1
    total = 0
    for i, char in enumerate(block):
        if char == '?':
            total += get_variations(tuple([block[:i], block[i + 1:]]), nums)
            total += get_variations(tuple([block[:i] + '#' + block[i + 1:]]), nums)
            break
    return total

def part_2(loc: str = DEFAULT_INPUT) -> int:
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            row, nums_str = line.rstrip().split(' ')
            row = '?'.join([row] * 5)
            row = tuple(section for section in row.split('.') if section)
            nums = tuple(map(int, nums_str.split(',')))
            lines.append((row, nums * 5))
    return sum(get_variations(*line) for line in lines)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
