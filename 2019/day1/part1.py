import math
def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        x.append(int(line))

    total_fuel = 0
    for n in x:
        fuel = math.floor(n/3) - 2
        total_fuel += fuel
    print(total_fuel)

if __name__ == '__main__':
    main()
