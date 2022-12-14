import ast
import functools


def parse_input(x):
    lefts = []
    rights = []
    for idx, i in enumerate(x):
        if idx % 3 == 0:
            lefts.append(ast.literal_eval(i))
        elif idx % 3 == 1:
            rights.append(ast.literal_eval(i))

    return lefts, rights


def part1(lefts, rights):
    valid_idxes = []
    for idx in range(len(lefts)):
        left = lefts[idx]
        right = rights[idx]
        result = compare_pairs(left, right)
        if result is True:# or result is None:
            valid_idxes.append(idx + 1)
    return sum(valid_idxes)

def compare_pairs(left, right):
    for i in range(len(left)):
        if len(right) < i + 1: #have run out of Right
            return False
        if isinstance(left[i], list) and isinstance(right[i], list):
            result = compare_pairs(left[i], right[i])
        elif isinstance(left[i], list) and isinstance(right[i], int):
            result = compare_pairs(left[i], [right[i]])
        elif isinstance(left[i], int) and isinstance(right[i], list):
            result = compare_pairs([left[i]], right[i])
        else:
            result = compare_valid(left[i], right[i])
        if result is True:
            return True
        elif result is False:
            return False
        else:
            pass

    # Check if left has run out
    if len(right) > len(left):
        return True


def compare_valid(left_val, right_val):
    if left_val < right_val:
        return True
    elif left_val > right_val:
        return False
    else:
        return 'inconclusive'

def part2(lefts, rights):
    all = lefts + rights + [[[2]]] + [[[6]]]
    def wrapped_compare_pairs(left, right):
        if compare_pairs(left,right) is True:
            return -1
        else:
            return 1
    sorted_l = sorted(all, key=functools.cmp_to_key(wrapped_compare_pairs))
    decoder_locations = []
    for idx, i in enumerate(sorted_l):
        if i == [[2]] or i ==[[6]]:
            decoder_locations.append(idx+1)
    return decoder_locations[0] * decoder_locations[1]


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    lefts, rights = parse_input(x)
    print(part1(lefts, rights))
    print(part2(lefts, rights))


if __name__ == '__main__':
    main()