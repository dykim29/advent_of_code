import numpy as np


def part1(x):
    x = np.array(x)
    flash_count = [0]
    for i in range(100):
        flash_history = np.zeros(x.shape)
        advance(x, flash_history, flash_count)
    return flash_count[0]


def part2(x):
    x = np.array(x)
    flash_count = [0]
    all_flashed = False
    step = 0
    while not all_flashed:
        step+=1
        flash_history = np.zeros(x.shape)
        advance(x, flash_history, flash_count)
        if np.all(flash_history == 1):
            all_flashed = True
    return step


def advance(x, flash_history, flash_count):
    for row in range(x.shape[0]):
        for col in range(x.shape[1]):
            add_one(x, row, col, flash_history, flash_count)


def add_one(x, row, col, flash_history, flash_count):
    if 0 <= row < x.shape[0] and 0 <= col < x.shape[1]:
        if x[row, col] == 0 and flash_history[row, col] == 1:
            pass
        elif x[row, col] == 9:
            x[row, col] = 0
            flash_history[row, col] = 1
            flash_count[0] += 1
            flash(x, row, col, flash_history, flash_count)
        else:
            x[row, col] += 1


def flash(x, row, col, flash_history, flash_count):
    for row_tmp in range(row-1, row+2):
        for col_tmp in range(col-1, col+2):
            if (row_tmp, col_tmp) != (row, col):
                add_one(x, row_tmp, col_tmp, flash_history, flash_count)


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = [[int(i) for i in string] for string in x]
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
