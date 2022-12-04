from typing import List
from functools import reduce

import numpy as np


def find_overlap(list_str: List[str]):
    overlap_inner = lambda x, y: set(x).intersection(set(y))
    overlap = list(reduce(overlap_inner, list_str))
    if len(overlap) > 1:
        raise NotImplementedError
    if len(overlap) == 0:
        raise Exception("no overlap found")
    return overlap[0]


def get_priority(x: str):
    if len(x) > 1:
        raise ValueError
    if x.isupper():
        return ord(x) - 38
    else:
        return ord(x) - 96


def part1(x):
    overlaps = []
    for i in x:
        comp1 = i[0:len(i) // 2]
        comp2 = i[len(i) // 2:]
        overlaps.append(find_overlap([comp1, comp2]))
    sum_priority = np.sum([get_priority(i) for i in overlaps])
    return sum_priority


def part2(x):
    overlaps = []
    i = 0
    while i < len(x):
        overlaps.append(find_overlap(x[i:i+3]))
        i += 3
    sum_priority = np.sum([get_priority(i) for i in overlaps])
    return sum_priority


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()