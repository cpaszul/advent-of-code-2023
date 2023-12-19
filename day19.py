from math import prod

DEFAULT_INPUT = 'day19.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    rules = {}
    with open(loc) as f:
        rules_raw, parts_raw = f.read().split('\n\n')
    for rule in rules_raw.split('\n'):
        label, flows = rule[:-1].split('{')
        rule_flows = []
        for flow in flows.split(','):
            if ':' in flow:
                test, dest = flow.split(':')
                field = test[0]
                op = test[1]
                n = int(test[2:])
                rule_flows.append([field, op, n, dest])
            else:
                rule_flows.append([flow])
        rules[label] = rule_flows
    parts = []
    for part in parts_raw.split('\n'):
        p = {}
        x, m, a, s = part[1:-1].split(',')
        p['x'] = int(x.split('=')[1])
        p['m'] = int(m.split('=')[1])
        p['a'] = int(a.split('=')[1])
        p['s'] = int(s.split('=')[1])
        parts.append(p)
    return sum(sum(part.values()) for part in parts if is_accepted(rules, 'in', part))

def is_accepted(rules: dict[str, list], r: str, part: dict[str, int]) -> bool:
    if r == 'A':
        return True
    if r == 'R':
        return False
    workflow = rules[r]
    for flow in workflow:
        if len(flow) > 1:
            field, op, n, dest = flow
            if (op == '<' and part[field] < n) or (op == '>' and part[field] > n):
                return is_accepted(rules, dest, part)
            continue
        else:
            return is_accepted(rules, flow[0], part)
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    starting_parts = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    rules = {}
    with open(loc) as f:
        rules_raw = f.read().split('\n\n')[0]
    for rule in rules_raw.split('\n'):
        label, flows = rule[:-1].split('{')
        rule_flows = []
        for flow in flows.split(','):
            if ':' in flow:
                test, dest = flow.split(':')
                field = test[0]
                op = test[1]
                n = int(test[2:])
                rule_flows.append([field, op, n, dest])
            else:
                rule_flows.append([flow])
        rules[label] = rule_flows
    return number_accepted(rules, 'in', starting_parts)

def number_accepted(rules: dict[str, list], r: str, parts: dict[str, tuple[int, int]]) -> int:
    if r == 'A':
        return valid_parts(parts)
    if r == 'R':
        return 0
    workflow = rules[r]
    accepted = 0
    for flow in workflow:
        if len(flow) > 1:
            field, op, n, dest = flow
            new_parts = parts.copy()
            if op == '<':
                new_parts[field] = (parts[field][0], n - 1)
                parts[field] = (n, parts[field][1])
            else:
                new_parts[field] = (n + 1, parts[field][1])
                parts[field] = (parts[field][0], n)
            accepted += number_accepted(rules, dest, new_parts)
        else:
            accepted += number_accepted(rules, flow[0], parts)
    return accepted

def valid_parts(parts: dict[str, tuple[int, int]]) -> int:
    return prod(max(0, (val_max - val_min + 1)) for val_min, val_max in parts.values())

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
