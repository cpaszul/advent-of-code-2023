from collections import defaultdict, deque
from math import lcm

DEFAULT_INPUT = 'day20.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    connects = {}
    types = {'broadcaster': 'broadcast'}
    flip_states = {}
    conj_states = defaultdict(dict)
    with open(loc) as f:
        for line in f.readlines():
            mod, dest = line.rstrip().split(' -> ')
            if mod == 'broadcaster':
                mod_name = 'broadcaster'
            else:
                mod_type = 'flip' if mod[0] == '%' else 'conj'
                mod_name = mod[1:]
                types[mod_name] = mod_type
                if mod_type == 'flip':
                    flip_states[mod_name] = False
            connects[mod_name] = dest.split(', ')
            for d in dest.split(', '):
                if d not in connects:
                    connects[d] = None
                if d not in types:
                    types[d] = None
    for source, dest_list in connects.items():
        if dest_list:
            for dest in dest_list:
                if types[dest] == 'conj':
                    conj_states[dest][source] = 'low'
    low = 0
    high = 0
    for _ in range(1000):
        d = deque([('broadcaster', 'button', 'low')])
        while d:
            dest_name, source_name, signal = d.popleft()
            if signal == 'low':
                low += 1
            else:
                high += 1
            dest_connects = connects[dest_name]
            if dest_connects is None:
                continue
            dest_type = types[dest_name]
            if dest_type == 'flip':
                if signal == 'high':
                    continue
                else:
                    flip_states[dest_name] = not flip_states[dest_name]
                    signal_to_send = 'high' if flip_states[dest_name] else 'low'
                    for connect in dest_connects:
                        d.append((connect, dest_name, signal_to_send))
            if dest_type == 'conj':
                conj_states[dest_name][source_name] = signal
                if all(value == 'high' for value in conj_states[dest_name].values()):
                    signal_to_send = 'low'
                else:
                    signal_to_send = 'high'
                for connect in dest_connects:
                    d.append((connect, dest_name, signal_to_send))
            if dest_type == 'broadcast':
                for connect in dest_connects:
                    d.append((connect, dest_name, signal))
    return low * high
                
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    connects = {}
    types = {'broadcaster': 'broadcast'}
    flip_states = {}
    conj_states = defaultdict(dict)
    with open(loc) as f:
        for line in f.readlines():
            mod, dest = line.rstrip().split(' -> ')
            if mod == 'broadcaster':
                mod_name = 'broadcaster'
            else:
                mod_type = 'flip' if mod[0] == '%' else 'conj'
                mod_name = mod[1:]
                types[mod_name] = mod_type
                if mod_type == 'flip':
                    flip_states[mod_name] = False
            connects[mod_name] = dest.split(', ')
            for d in dest.split(', '):
                if d not in connects:
                    connects[d] = None
                if d not in types:
                    types[d] = None
    for source, dest_list in connects.items():
        if dest_list:
            for dest in dest_list:
                if types[dest] == 'conj':
                    conj_states[dest][source] = 'low'
    for mod in connects:
        if connects[mod] and 'rx' in connects[mod]:
            needed_conj = mod
            needed_mods = {key: -1 for key in conj_states[mod].keys()}
    i = 0
    while True:
        d = deque([('broadcaster', 'button', 'low')])
        i += 1
        while d:
            dest_name, source_name, signal = d.popleft()
            if dest_name == needed_conj and signal == 'high':
                if needed_mods[source_name] == -1:
                    needed_mods[source_name] = i
            if all(value != -1 for value in needed_mods.values()):
                return lcm(*needed_mods.values())
            dest_connects = connects[dest_name]
            if dest_connects is None:
                continue
            dest_type = types[dest_name]
            if dest_type == 'flip':
                if signal == 'high':
                    continue
                else:
                    flip_states[dest_name] = not flip_states[dest_name]
                    signal_to_send = 'high' if flip_states[dest_name] else 'low'
                    for connect in dest_connects:
                        d.append((connect, dest_name, signal_to_send))
            if dest_type == 'conj':
                conj_states[dest_name][source_name] = signal
                if all(value == 'high' for value in conj_states[dest_name].values()):
                    signal_to_send = 'low'
                else:
                    signal_to_send = 'high'
                for connect in dest_connects:
                    d.append((connect, dest_name, signal_to_send))
            if dest_type == 'broadcast':
                for connect in dest_connects:
                    d.append((connect, dest_name, signal))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
