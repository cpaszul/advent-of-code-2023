from collections import defaultdict, deque, namedtuple

DEFAULT_INPUT = 'day22.txt'

Brick = namedtuple('Brick', ['num', 'points'])
Point = namedtuple('Point', ['x', 'y', 'z'])
        
def day_22(loc: str = DEFAULT_INPUT) -> int:
    bricks = []
    brick_nums = []
    with open(loc) as f:
        for i, line in enumerate(f.readlines()):
            x_a, y_a, z_a, x_b, y_b, z_b = map(int, line.rstrip().replace('~', ',').split(','))
            if (x_a, y_a, z_a) == (x_b, y_b, z_b):
                brick_set = {Point(x_a, y_a, z_a)}
            else:
                brick_set = set()
                if x_a != x_b:
                    for x in range(min(x_a, x_b), max(x_a, x_b) + 1):
                        brick_set.add(Point(x, y_a, z_a))
                if y_a != y_b:
                    for y in range(min(y_a, y_b), max(y_a, y_b) + 1):
                        brick_set.add(Point(x_a, y, z_a))
                if z_a != z_b:
                    for z in range(min(z_a, z_b), max(z_a, z_b) + 1):
                        brick_set.add(Point(x_a, y_a, z))
            bricks.append(Brick(i, brick_set))
            brick_nums.append(i)
    bricks.sort(key=lowest_z)
    settled_bricks = []
    depends = defaultdict(set)
    for brick in bricks:
        if lowest_z(brick) == 1:
            settled_bricks.append(brick)
            continue
        settled = False
        i = 1
        while not settled:
            prev_brick = Brick(brick.num, {Point(p.x, p.y, p.z - (i - 1)) for p in brick.points})
            new_brick = Brick(brick.num, {Point(p.x, p.y, p.z - i) for p in brick.points})
            for br in settled_bricks:
                if intersect(br, new_brick):
                    depends[new_brick.num].add(br.num)
                    settled = True
            if settled == True:
                settled_bricks.append(prev_brick)
                continue
            if lowest_z(new_brick) == 1:
                settled_bricks.append(new_brick)
                settled = True
                continue
            i += 1
    can_delete = 0
    for num in brick_nums:
        if any(value == {num} for value in depends.values()):
            continue
        can_delete += 1
    return can_delete, sum(chain_reaction(depends, n) for n in brick_nums)

def lowest_z(br: type[Brick]) -> int:
    return min(br.points, key=lambda point: point.z).z

def intersect(brick_a: type[Brick], brick_b: type[Brick]) -> bool:
    return len(brick_a.points & brick_b.points) != 0

def chain_reaction(depends_orig: dict[int, set[int]], n: int) -> int:
    depends = {k:v.copy() for k, v in depends_orig.items()}
    to_delete = deque([n])
    to_fall = set()
    while to_delete:
        current = to_delete.popleft()
        for dep in depends:
            if current in depends[dep]:
                depends[dep].remove(current)
                if not depends[dep]:
                    if dep not in to_fall:
                        to_fall.add(dep)
                        to_delete.append(dep)
    return len(to_fall)

if __name__ == '__main__':
    part_1, part_2 = day_22()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
