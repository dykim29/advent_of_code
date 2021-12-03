import numpy as np

def part1(x):
    gamma_binary_string = find_most_common(x)
    epsilon_binary_string = ''.join(['0' if i=='1' else '1' for i in gamma_binary_string])
    return int(gamma_binary_string, 2) * int(epsilon_binary_string, 2)


def find_most_common(x):
    y = [[int(i) for i in j] for j in x]
    y = np.array(y)
    sums = (np.sum(y, axis=0)/y.shape[0])
    return ''.join([str(int(i)) for i in sums >= 0.5])


def find_least_common(x):
    t = find_most_common(x)
    return ''.join(['0' if i == '1' else '1' for i in t])


def part2(x):
    j = set(x)
    for idx in range(0, len(x[0])):
        most_common = find_most_common(list(j))
        to_keep = [keep for keep in j if keep[idx] == most_common[idx]]
        j = set(to_keep)
        if len(j) == 1:
            break
    oxygen = int(list(j)[0], 2)

    j = set(x)
    for idx in range(0, len(x[0])):
        least_common = find_least_common(list(j))
        to_keep = [keep for keep in j if keep[idx] == least_common[idx]]
        j = set(to_keep)
        if len(j) == 1:
            break
    CO2 = int(list(j)[0], 2)
    return oxygen * CO2


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))

if __name__ == '__main__':
    main()