from collections import Counter

import numpy as np


def part1(x):
    positions = [int(i) for i in x[0].split(',')]
    pos_counter = Counter(positions)

    possible_positions = range(min(positions), max(positions))

    fuels = []
    for i in possible_positions:
        fuel = 0
        for pos, total_no in pos_counter.items():
            fuel += abs(i-pos) * total_no
        fuels.append(fuel)
    return np.min(fuels)

def part2(x):
    positions = [int(i) for i in x[0].split(',')]
    pos_counter = Counter(positions)
    possible_positions = range(min(positions), max(positions))
    # First generate a dictionary containing how much fuel would be needed for each step size.
    step_size = 0
    f1 = 0
    fuel_needed = {}
    while step_size <= max(positions) - min(positions):
        f2 = f1 + step_size
        fuel_needed[step_size] = f2
        f1 = f2
        step_size += 1

    fuels = []
    for i in possible_positions:
        fuel = 0
        for pos, total_no in pos_counter.items():
            fuel += fuel_needed[abs(i-pos)] * total_no
        fuels.append(fuel)
    return np.min(fuels)

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
