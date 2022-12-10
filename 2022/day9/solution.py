import numpy as np


def parse_input(x):
    y = []
    for i in x:
        y.append((i[0], int(i[2:])))
    return y


def move_head(position: np.array, dir):
    if dir == 'R':
        mov = np.array([0, 1])
    elif dir == 'L':
        mov = np.array([0, -1])
    elif dir == 'U':
        mov = np.array([1, 0])
    elif dir == 'D':
        mov = np.array([-1, 0])
    else:
        raise Exception('Unknown movement')
    return position + mov


def move_tail(head_pos, tail_pos):
    diff = head_pos - tail_pos
    if diff.dot(diff) <= 1:
        return tail_pos
    elif abs(diff[0]) == 1 and abs(diff[1]) == 1:
        return tail_pos
    elif diff[0] == 0:
        return tail_pos + np.array([0, diff[1]// abs(diff[1])])
    elif diff[1] == 0:
        return tail_pos + np.array([diff[0]//abs(diff[0]), 0])
    else:
        mov = np.array([diff[0] // abs(diff[0]), diff[1] // abs(diff[1])])
        return tail_pos + mov


def part1(x):
    tail_visits = {(0, 0)}
    head_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])
    for dir, n_step in x:
        for i in range(n_step):
            head_pos = move_head(head_pos, dir)
            tail_pos = move_tail(head_pos, tail_pos)
            tail_visits.add(tuple(tail_pos))
    return len(tail_visits)


def part2(x):
    tail_visits = {(0, 0)}
    positions = {i: np.array([0, 0]) for i in range(10)}
    for dir, n_step in x:
        for i in range(n_step):
            positions[0] = move_head(positions[0], dir)
            for rope_segment_idx in range(1, 10):
                positions[rope_segment_idx] = move_tail(positions[rope_segment_idx - 1], positions[rope_segment_idx])
            tail_visits.add(tuple(positions[9]))
    return len(tail_visits)


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
