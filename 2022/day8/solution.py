import numpy as np


def parse_input(x):
    return np.array([[int(i) for i in j] for j in x])


def part1(x: np.ndarray):
    n_visible = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            visible_from_above = all(x[:i, j] < x[i, j])
            visible_from_left = all(x[i, :j] < x[i, j])
            visible_from_below = all(x[i+1:, j] < x[i, j])
            visible_from_right = all(x[i, j+1:] < x[i, j])
            n_visible += visible_from_above or visible_from_right or visible_from_left or visible_from_below
    return n_visible

def get_viewing_distance(val, arr):
    if len(arr) == 0:
        return 0
    for idx, tree in enumerate(arr):
        if tree >= val:
            return idx + 1
    return len(arr)

def part2(x):
    max_scenic_dist = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            viewing_dist_above = get_viewing_distance(x[i, j], x[:i, j][::-1])
            viewing_dist_left = get_viewing_distance(x[i, j], x[i, :j][::-1])
            viewing_dist_below = get_viewing_distance(x[i, j], x[i+1:, j])
            viewing_dist_right = get_viewing_distance(x[i, j], x[i, j+1:])
            max_scenic_dist = max(max_scenic_dist, viewing_dist_above * viewing_dist_left * viewing_dist_below
                                  * viewing_dist_right)
    return max_scenic_dist

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()