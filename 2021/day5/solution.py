import numpy as np


def parse_input(x):
    vents = []
    for line in x:
        start = [int(i) for i in line.split(' -> ')[0].split(',')]
        end = [int(i) for i in line.split(' -> ')[1].split(',')]
        vents.append([start, end])
    return vents


def part1(x):
    vents = parse_input(x)
    grid = np.zeros((1000, 1000))
    for vent in vents:
        x1, y1 = vent[0]
        x2, y2 = vent[1]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[x1, i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[i, y1] += 1
    return (grid>=2).sum()

def part2(x):

    vents = parse_input(x)
    grid = np.zeros((1000, 1000))
    for vent in vents:
        x1, y1 = vent[0]
        x2, y2 = vent[1]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[x1, i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[i, y1] += 1
        else:
            x_step_direction = np.sign(x2 - x1)
            y_step_direction = np.sign(y2 - y1)
            n_steps = abs(x2-x1)
            for i in range(n_steps + 1):
                grid[x1 + i*x_step_direction, y1 + i*y_step_direction] += 1
    return (grid >= 2).sum()


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()