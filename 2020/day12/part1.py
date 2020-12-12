from collections import defaultdict
import numpy as np

directions = {
    'N': np.array([0, 1]),
    'S': np.array([0, -1]),
    'W': np.array([-1, 0]),
    'E': np.array([1, 0])
}

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    current_facing_direction = np.array([1, 0])
    position = np.array([0,0])

    for i in x:
        direction = i[0]
        number = int(i[1:])
        if direction == 'F':
            position = position + current_facing_direction * number
        elif direction in ['N', 'S', 'W', 'E']:
            position = position + directions[direction] * number
        elif direction in ['R', 'L']:
            current_facing_direction = rotate_vector(current_facing_direction, direction, number)

    manhatten_distance = abs(position[0]) + abs(position[1])
    print(manhatten_distance)


def rotate_vector(vector_in, direction, degree):
    if direction == 'R':
        degree = 360 - degree
    radians = degree * np.pi/180
    x = vector_in[0] * np.cos(radians) - vector_in[1] * np.sin(radians)
    y = vector_in[0] * np.sin(radians) + vector_in[1] * np.cos(radians)
    return np.array([x, y])

if __name__ == '__main__':
    main()