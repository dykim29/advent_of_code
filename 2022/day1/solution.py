import numpy as np

def parse_input(x):
    y = [[]]
    for i in x:
        if i != '':
            y[-1].append(int(i))
        else:
            y.append([])
    return y


def part1(x):
    sums = []
    for i in x:
        sums.append(np.sum(i))
    return np.max(sums)


def part2(x):
    sums = []
    for i in x:
        sums.append(np.sum(i))
    sorted = np.sort(sums)[::-1]
    return np.sum(sorted[:3])


def main():
    f = open("input_test.txt", "r")
    x = f.read().splitlines()
    parsed = parse_input(x)
    print(part1(parsed))
    print(part2(parsed))


if __name__ == '__main__':
    main()