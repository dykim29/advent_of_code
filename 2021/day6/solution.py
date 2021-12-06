from collections import Counter


def part1(x):
    """
    The inefficient solution
    """
    x = [int(i) for i in x[0].split(',')]
    n_days = 80
    for n_day in range(n_days):
        n_new_fish = 0
        for idx in range(len(x)):
            if x[idx] == 0:
                x[idx] = 6
                n_new_fish += 1
            else:
                x[idx] -= 1
        x.extend([8]*n_new_fish)

    return len(x)


def part2(x):
    """
    The efficient solution
    """
    x = [int(i) for i in x[0].split(',')]
    fish_timer_counter = Counter(x)
    n_days = 256
    for n_day in range(n_days):
        copy = fish_timer_counter.copy()
        fish_timer_counter[8] = copy[0]
        for day in range(0, 8):
            if day == 6:
                fish_timer_counter[day] = copy[7] + copy[0]
            else:
                fish_timer_counter[day] = copy[day+1]
    return sum(fish_timer_counter.values())


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
