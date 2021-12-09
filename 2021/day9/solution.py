from collections import Counter

import numpy as np


def parse_input(x):
    y = []
    for i in x:
        y.append([int(j) for j in i])
    return np.array(y)


def part1(x: np.ndarray):
    n_row, n_col = x.shape
    sum = 0
    for row in range(n_row):
        for col in range(n_col):
            if is_low_point(x, row, col):
                sum += x[row, col] + 1
    return sum

def is_low_point(x, row, col):
    above = get_point_value_default_inf(x, row-1, col)
    below = get_point_value_default_inf(x, row+1, col)
    left = get_point_value_default_inf(x, row, col-1)
    right = get_point_value_default_inf(x, row, col+1)
    current = x[row, col]

    return current < above and current < below and current< left and current < right


def get_point_value_default_inf(x, row, col):
    if 0 <= row < x.shape[0] and 0 <= col < x.shape[1]:
        return x[row, col]
    else:
        return np.inf


def part2(x):
    n_row, n_col = x.shape
    basin_points = Counter()
    for row in range(n_row):
        for col in range(n_col):
            if x[row, col] < 9:
                low_point = find_next_flow_point(x, row, col)
                basin_points[low_point] += 1
    return np.prod([i[-1] for i in basin_points.most_common(3)])


def find_next_flow_point(x, row, col):
    current = x[row, col]
    above = get_point_value_default_inf(x, row-1, col)
    below = get_point_value_default_inf(x, row+1, col)
    left = get_point_value_default_inf(x, row, col-1)
    right = get_point_value_default_inf(x, row, col+1)
    if above < current:
        return find_next_flow_point(x, row-1, col)
    elif below < current:
        return find_next_flow_point(x, row+1, col)
    elif left < current:
        return find_next_flow_point(x, row, col-1)
    elif right < current:
        return find_next_flow_point(x, row, col+1)
    else:
        return (row, col)


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
