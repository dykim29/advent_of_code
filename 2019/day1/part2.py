import math

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    total_fuel = 0
    for n in x:
        fuel = int(n)
        while fuel >= 0:
            fuel = calc_fuel(fuel)
            if fuel > 0:
                total_fuel += fuel
            print(fuel, total_fuel)

    print(total_fuel)

def calc_fuel(n):
    return math.floor(n/3) - 2

if __name__ == '__main__':
    main()
