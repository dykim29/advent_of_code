def part1(x):
    count = 0
    for idx in range(1, len(x)):
        if x[idx] > x[idx - 1]:
            count += 1
    return count


def part2(x):
    count = 0
    for idx in range(1, len(x)-2):
        if x[idx+2] > x[idx - 1]:
            count += 1
    return count

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = [int(i) for i in x]
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()