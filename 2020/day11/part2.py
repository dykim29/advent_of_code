from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    y = []
    for row in x:
        y.append(list(row))
    y = np.array(y)
#    n = count_occupied_seats(y, 3, 3)
#    print(n)

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
                if n_occupied >= 5:
                    x_new[row][col] = 'L'
    return x_new

vision_movements = {
    'u': [-1, 0],
    'd': [1, 0],
    'r': [0, 1],
    'l': [0, -1],
    'ul': [-1, -1],
    'ur': [-1, 1],
    'dl': [1, -1],
    'dr': [1, 1]
}

def count_occupied_seats(x, row_in, col_in):
    n_rows, n_cols = x.shape
    count = 0
    for dir, movement in vision_movements.items():
        row = row_in
        col = col_in
        status = None
        while 0 <= row < n_rows and 0 <= col < n_cols and (status is None):
            row += movement[0]
            col += movement[1]
            status = check_occupied(x, row, col)
        if status == 'occupied':
            count += 1


    return count

def check_occupied(x, row, col):
    n_rows, n_cols = x.shape
    if 0 <= row < n_rows and 0 <= col < n_cols:
        if x[row][col] == '#':
            return 'occupied'
        elif x[row][col] == 'L':
            return 'empty'
        else:
            return None

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