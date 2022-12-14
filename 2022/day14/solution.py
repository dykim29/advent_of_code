import ast

import numpy as np


def parse_input(x):
    max_y = 0
    max_x = 0
    y = []
    for i in x:
        ls = i.split(' -> ')
        ls = [list(ast.literal_eval(k)) for k in ls]
        y.append(ls)

        max_y = max(max([k[1] for k in ls]), max_y)
        max_x = max(max([k[0] for k in ls]), max_x)
    grid = np.full((max_x + 1, max_y + 1), '.')
    for i in y:
        for idx in range(len(i) - 1):
            start = i[idx]
            end = i[idx + 1]
            if start[0] == end[0]:
                grid[start[0], min(start[1], end[1]): max(start[1], end[1]) + 1] = '#'
            elif start[1] == end[1]:
                grid[min(start[0], end[0]): max(start[0], end[0]) + 1, start[1]] = '#'

    return grid


def part1(grid):
    cur = (500, 0)
    while cur[1] + 1 < grid.shape[1] and cur[0] + 1 < grid.shape[0]:
        if grid[cur[0], cur[1] + 1] == ".":
            cur = (cur[0], cur[1] + 1)
        elif grid[cur[0] - 1, cur[1] + 1] == ".":
            cur = (cur[0] - 1, cur[1] + 1)
        elif grid[cur[0] + 1, cur[1] + 1] == ".":
            cur = (cur[0] + 1, cur[1] + 1)
        else:
            grid[cur] = 'O'
            cur = (500, 0)
        # print(grid[494:505, :].T)
    return (grid == 'O').sum()


def part2(grid):
    y_max = grid.shape[1] - 1
    grid = np.append(grid, np.full((grid.shape[0], 2), '.'), 1)
    grid = np.append(grid, np.full((200, grid.shape[1]), '.'), 0)
    grid[:, y_max + 2] = '#'

    cur = (500, 0)
    while True:
        if grid[cur[0], cur[1] + 1] == ".":
            cur = (cur[0], cur[1] + 1)
        elif grid[cur[0] - 1, cur[1] + 1] == ".":
            cur = (cur[0] - 1, cur[1] + 1)
        elif grid[cur[0] + 1, cur[1] + 1] == ".":
            cur = (cur[0] + 1, cur[1] + 1)
        else:
            if cur == (500, 0):
                break
            grid[cur] = 'O'
            cur = (500, 0)
    return (grid == 'O').sum() + 1


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
