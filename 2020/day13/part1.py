from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    current_time = int(x[0])
    y = x[1].split(',')

    next_arrival_times = []
    buses = []
    for bus in y:
        if bus != 'x':
            next_arrival_times.append(current_time + ( int(bus) - (current_time % int(bus)) ))
            buses.append(int(bus))
    i = np.argmin(next_arrival_times)
    print(buses[i] * (next_arrival_times[i] - current_time))

if __name__ == '__main__':
    main()