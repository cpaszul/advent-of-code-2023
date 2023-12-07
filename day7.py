from functools import cmp_to_key

DEFAULT_INPUT = 'day7.txt'

def day_7(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        hands = [line.rstrip().split(' ') for line in f.readlines()]
    hands.sort(key=cmp_to_key(comp_hands))
    part_one_result = sum(int(hand[1]) * (ind + 1) for ind, hand in enumerate(hands))
    hands.sort(key=cmp_to_key(comp_hands_joker))
    return part_one_result, \
           sum(int(hand[1]) * (ind + 1) for ind, hand in enumerate(hands))

def comp_hands(hand_one: tuple[str, str], hand_two: tuple[str, str]) -> int:
    h_one = hand_one[0]
    h_two = hand_two[0]
    order = 'AKQJT98765432'
    if hand_type(h_one) == hand_type(h_two):
        for char_one, char_two in zip(h_one, h_two):
            if char_one != char_two:
                return order.index(char_two) - order.index(char_one)
        return 0
    return hand_type(h_one) - hand_type(h_two)

def hand_type(hand: str) -> int:
    if len(set(hand)) == 1:
        return 6
    if len(set(hand)) == 2:
        if hand.count(hand[0]) in [1, 4]:
            return 5
        return 4
    if len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            return 3
        return 2
    if len(set(hand)) == 4:
        return 1
    return 0

def comp_hands_joker(hand_one: tuple[str, str], hand_two: tuple[str, str]) -> int:
    h_one = hand_one[0]
    h_two = hand_two[0]
    order = 'AKQT98765432J'
    if hand_type_joker(h_one) == hand_type_joker(h_two):
        for char_one, char_two in zip(h_one, h_two):
            if char_one != char_two:
                return order.index(char_two) - order.index(char_one)
        return 0
    return hand_type_joker(h_one) - hand_type_joker(h_two)

def hand_type_joker(hand: str) -> int:
    if 'J' not in hand or hand == 'JJJJJ':
        return hand_type(hand)
    non_jokers = set(char for char in hand if char != 'J')
    return max([hand_type(hand.replace('J', char)) for char in non_jokers])

if __name__ == '__main__':
    part_1, part_2 = day_7()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
