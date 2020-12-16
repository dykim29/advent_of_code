from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    current_time = int(x[0])
    y = x[1].split(',')

    buses = {}
    B = [(int(y[k]), k) for k in range(len(y)) if y[k] != 'x']

    lcm = 1
    time = 0
    for i in range(len(B) - 1):
        bus_id = B[i + 1][0]
        idx = B[i + 1][1]
        lcm *= B[i][0]
        print(bus_id, idx, lcm, time)
        while (time + idx) % bus_id != 0:
            print(time)
            time += lcm
    print(time)


if __name__ == '__main__':
    main()