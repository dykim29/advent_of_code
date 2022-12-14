import numpy as np
from collections import defaultdict


def parse_input(x):
    y = []
    for row, i in enumerate(x):
        for col, j in enumerate(i):
            if j == 'S':
                starting_pos = (row, col)
            elif j == 'E':
                end_pos = (row, col)
        y.append([k for k in i])
    y = np.array(y)
    # make S equal to a so it can move anywhere
    y[starting_pos] = 'a'
    y[end_pos] = 'z'
    return np.array(y), starting_pos, end_pos



def part1(x, start, end):
    min_length_to_here = defaultdict(lambda: np.inf)
    visited = ()

    def move(pos, n_steps, visited):
        if n_steps < min_length_to_here[pos]:
            min_length_to_here[pos] = n_steps
        else:
            return
        if pos == end:
            return
        else:
            visited = visited + (pos,)

        if 0 <= pos[1] + 1 < x.shape[1] and ord(x[pos[0], pos[1]+1]) - ord(x[pos]) <= 1 and (pos[0], pos[1]+1) not in visited:
            move((pos[0], pos[1] + 1), n_steps+1, visited)
        if 0 <= pos[1] - 1 < x.shape[1] and ord(x[pos[0], pos[1]-1]) - ord(x[pos]) <= 1 and (pos[0], pos[1]-1) not in visited:
            move((pos[0], pos[1] - 1), n_steps+1, visited)
        if 0 <= pos[0] - 1 < x.shape[0] and ord(x[pos[0] - 1, pos[1]]) - ord(x[pos]) <= 1 and (pos[0] - 1, pos[1]) not in visited:
            move((pos[0] - 1, pos[1]), n_steps+1, visited)
        if 0 <= pos[0] + 1 < x.shape[0] and ord(x[pos[0] + 1, pos[1]]) - ord(x[pos]) <= 1 and (pos[0] + 1, pos[1]) not in visited:
            move((pos[0] + 1, pos[1]), n_steps+1, visited)

    move(start, 0, visited)
    return min_length_to_here[end]


def part2(x, start, end):
    min_length_to_here = defaultdict(lambda: np.inf)
    visited = ()
    possible_lengths = []
    # Not the nicest solution ....
    max_steps = 400

    def move(pos, n_steps, visited):
        if n_steps == max_steps:
            return
        if n_steps < min_length_to_here[pos]:
            min_length_to_here[pos] = n_steps
        else:
            return
        if x[pos] == 'a':
            possible_lengths.append(n_steps)
            return
        else:
            visited = visited + (pos,)

        if 0 <= pos[1] + 1 < x.shape[1] and ord(x[pos[0], pos[1]+1]) - ord(x[pos]) >= -1 and (pos[0], pos[1]+1) not in visited:
            move((pos[0], pos[1] + 1), n_steps+1, visited)
        if 0 <= pos[1] - 1 < x.shape[1] and ord(x[pos[0], pos[1]-1]) - ord(x[pos]) >= -1 and (pos[0], pos[1]-1) not in visited:
            move((pos[0], pos[1] - 1), n_steps+1, visited)
        if 0 <= pos[0] - 1 < x.shape[0] and ord(x[pos[0] - 1, pos[1]]) - ord(x[pos]) >= -1 and (pos[0] - 1, pos[1]) not in visited:
            move((pos[0] - 1, pos[1]), n_steps+1, visited)
        if 0 <= pos[0] + 1 < x.shape[0] and ord(x[pos[0] + 1, pos[1]]) - ord(x[pos]) >= -1 and (pos[0] + 1, pos[1]) not in visited:
            move((pos[0] + 1, pos[1]), n_steps+1, visited)

    move(end, 0, visited)
    return min(possible_lengths)

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x, start, end = parse_input(x)
    print(part1(x, start, end))
    print(part2(x, start, end))


if __name__ == '__main__':
    main()