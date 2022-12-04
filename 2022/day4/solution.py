from typing import List
from functools import reduce

import numpy as np

def find_range(y: str) -> list:
    """
    Args
        y: string like '1-6' indicating range
    Returns
        all ints in between, e.g. [1, 2, 3, 4, 5, 6]
    """
    start = int(y.split('-')[0])
    end = int(y.split('-')[1])
    return list(range(start, end+1))


def parse_input(x):
    y = []
    for i in x:
        a1, a2 = i.split(',')
        y.append([find_range(a1), find_range(a2)])
    return y


def part1(x: List[List[List[int]]]):
    n_fully_contained = 0
    for assignments in x:
        assignment1 = assignments[0]
        assignment2 = assignments[1]
        if len(set(assignment1).intersection(assignment2)) == min(len(assignment1), len(assignment2)):
            n_fully_contained += 1
    return n_fully_contained


def part2(x):
    n_overlaps = 0
    for assignments in x:
        assignment1 = assignments[0]
        assignment2 = assignments[1]
        if len(set(assignment1).intersection(assignment2)) > 0:
            n_overlaps += 1
    return n_overlaps

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()