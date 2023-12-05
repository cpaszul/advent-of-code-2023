DEFAULT_INPUT = 'day5.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        seeds_raw, sts, stf, ftw, wtl, ltt, tth, htl = f.read().split('\n\n')
    seeds = list(map(int, seeds_raw.split(': ')[1].split(' ')))
    sts = [tuple(map(int, line.split(' '))) for line in sts.rstrip().split('\n')[1:]]
    stf = [tuple(map(int, line.split(' '))) for line in stf.rstrip().split('\n')[1:]]
    ftw = [tuple(map(int, line.split(' '))) for line in ftw.rstrip().split('\n')[1:]]
    wtl = [tuple(map(int, line.split(' '))) for line in wtl.rstrip().split('\n')[1:]]
    ltt = [tuple(map(int, line.split(' '))) for line in ltt.rstrip().split('\n')[1:]]
    tth = [tuple(map(int, line.split(' '))) for line in tth.rstrip().split('\n')[1:]]
    htl = [tuple(map(int, line.split(' '))) for line in htl.rstrip().split('\n')[1:]]
    min_location = 10**9
    for seed in seeds:
        soil = get_dest(seed, sts)
        fert = get_dest(soil, stf)
        water = get_dest(fert, ftw)
        light = get_dest(water, wtl)
        temp = get_dest(light, ltt)
        humid = get_dest(temp, tth)
        loc = get_dest(humid, htl)
        min_location = min(min_location, loc)
    return min_location

def get_dest(source: int, lines: list[tuple[int, int, int]]) -> int:
    for d, s, r in lines:
        if s <= source < (s + r):
            return d + source - s
    return source

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        seeds_raw, sts, stf, ftw, wtl, ltt, tth, htl = f.read().split('\n\n')
    seeds = map(int, seeds_raw.split(': ')[1].split(' '))
    seeds = list(zip(*[iter(seeds)]*2))
    sts = [tuple(map(int, line.split(' '))) for line in sts.rstrip().split('\n')[1:]]
    stf = [tuple(map(int, line.split(' '))) for line in stf.rstrip().split('\n')[1:]]
    ftw = [tuple(map(int, line.split(' '))) for line in ftw.rstrip().split('\n')[1:]]
    wtl = [tuple(map(int, line.split(' '))) for line in wtl.rstrip().split('\n')[1:]]
    ltt = [tuple(map(int, line.split(' '))) for line in ltt.rstrip().split('\n')[1:]]
    tth = [tuple(map(int, line.split(' '))) for line in tth.rstrip().split('\n')[1:]]
    htl = [tuple(map(int, line.split(' '))) for line in htl.rstrip().split('\n')[1:]]
    loc = 0
    while True:
        humid = get_source(loc, htl)
        temp = get_source(humid, tth)
        light = get_source(temp, ltt)
        water = get_source(light, wtl)
        fert = get_source(water, ftw)
        soil = get_source(fert, stf)
        seed = get_source(soil, sts)
        if valid_seed(seed, seeds):
            return loc
        loc += 1

def get_source(dest: int, lines: list[tuple[int, int, int]]) -> int:
    for d, s, r in lines:
        if d <= dest < (d + r):
            return s + dest - d
    return dest

def valid_seed(seed: int, seeds: list[tuple[int, int]]) -> bool:
    for start, length in seeds:
        if start <= seed < (start + length):
            return True
    return False

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
