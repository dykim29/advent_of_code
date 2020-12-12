from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    y = []
    for row in x:
        y.append(list(row))
    y = np.array(y)
    y = run_algorithm(y)
    n_occupied_total = count_all_occupied_seats(y)
    print(n_occupied_total)


def run_algorithm(y):
    while True:
        y_next = occupy(y)
        y_next = move(y_next)
        if (y_next == y).all():
            return y
        y = y_next.copy()




def occupy(x):
    x_new = x.copy()
    n_rows, n_cols = x.shape
    for row in range(n_rows):
        for col in range(n_cols):
            if x[row][col] == 'L':
                n_occupied = count_occupied_seats(x, row, col)
                if n_occupied == 0:
                    x_new[row][col] = '#'
    return x_new

def move(x):
    x_new = x.copy()
    n_rows, n_cols = x.shape
    for row in range(n_rows):
        for col in range(n_cols):
            if x[row][col] == '#':
                n_occupied = count_occupied_seats(x, row, col)
                if n_occupied >= 4:
                    x_new[row][col] = 'L'
    return x_new


def count_occupied_seats(x, row_in, col_in):
    count = 0
    for row in range(row_in-1, row_in+2):
        for col in range(col_in-1, col_in+2):
            if not (row == row_in and col == col_in):
                count += check_occupied(x, row, col)
    return count

def check_occupied(x, row, col):
    n_rows, n_cols = x.shape
    if 0 <= row < n_rows and 0 <= col < n_cols:
        return x[row][col] == '#'
    else:
        return False

def count_all_occupied_seats(x):
    count = 0
    n_rows, n_cols = x.shape
    for row in range(n_rows):
        for col in range(n_cols):
            if x[row][col] == '#':
                count += 1
    return count

if __name__ == '__main__':
    main()