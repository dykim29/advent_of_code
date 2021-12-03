def part1(x:list):
    position = [0, 0] # horizontal, depth
    for command in x:
        direction, step_length = command.split(' ')
        step_length = int(step_length)
        if direction == 'forward':
            position[0] += step_length
        elif direction == 'up':
            position[1] += step_length
        elif direction == 'down':
            position[1] -= step_length
        else:
            raise Exception('Unknown direction')
    return - position[0] * position[1]


def part2(x: list):
    position = [0, 0, 0] # horizontal, depth, aim
    for command in x:
        direction, step_length = command.split(' ')
        step_length = int(step_length)
        if direction == 'forward':
            position[0] += step_length
            position[1] += position[2] * step_length
        elif direction == 'up':
            position[2] -= step_length
        elif direction == 'down':
            position[2] += step_length
        else:
            raise Exception('Unknown direction')
    print(position)
    return position[0] * position[1]

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))

if __name__ == '__main__':
    main()