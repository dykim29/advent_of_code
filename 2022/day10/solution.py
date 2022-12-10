
def check_signal(i, X, sum_signal):
    if (i - 20) % 40 == 0:
        return sum_signal + i * X
    else:
        return sum_signal


def part1(x):
    X = 1
    i = 0
    sum_signal_strength = 0
    for inst in x:
        if inst[:4] == 'noop':
            i += 1
            sum_signal_strength = check_signal(i, X, sum_signal_strength)
        elif inst[:4] == 'addx':
            for j in range(2):
                i += 1
                sum_signal_strength = check_signal(i, X, sum_signal_strength)
            X += int(inst[5:])
    return sum_signal_strength


def draw_crt(crt_panel, i, X):
    pos_of_crt_pixel_being_drawn = i % 40
    if X - 1 <= pos_of_crt_pixel_being_drawn <= X + 1:
        crt_panel[i//40][pos_of_crt_pixel_being_drawn] = '#'


def part2(x):
    crt_panel = [['.' for i in range(40)] for j in range(6)]
    X = 1
    i = 0
    for inst in x:
        if inst[:4] == 'noop':
            draw_crt(crt_panel, i, X)
            i += 1
        elif inst[:4] == 'addx':
            for j in range(2):
                draw_crt(crt_panel, i, X)
                i += 1
            X += int(inst[5:])
    for i in crt_panel:
        print(''.join(i))


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    part2(x)


if __name__ == '__main__':
    main()
