from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    values = {}

    for i in x:
        if i[0:4] == 'mask':
            mask = [elem for elem in i[7:]]
        else:
            address = int(i.split('[')[1].split(']')[0])
            value = int(i.split('= ')[1])
            values[address] = apply_value(mask, value)
    sum = 0
    for item in values:
        sum += values[item]
    print(sum)


def apply_value(mask, value):
    binary_value = dec_to_bin(value)
    binary_string = '0'*(36-len(str(binary_value))) + str(binary_value)
    for i in range(len(mask)):
        if mask[i] != 'X':
            binary_string = binary_string[:i] + mask[i] + binary_string[i+1:]
    return int(binary_string, 2)


def dec_to_bin(x):
    return int(bin(x)[2:])



if __name__ == '__main__':
    main()