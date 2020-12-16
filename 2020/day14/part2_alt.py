from collections import defaultdict
import numpy as np
import itertools

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    values = {}
#    masks = find_possible_masks('000X00000000000000000000000000X1001X')
#    print(masks)
#    for mask in masks:
#        add = find_addresses(42, mask)
#        print(add)


    for index, i in enumerate(x):
        print('doing line number {}'.format(index))
        if i[0:4] == 'mask':
            mask = i[7:].replace('0', 'Y')
            possible_masks = find_possible_masks(mask)
        else:
            address = int(i.split('[')[1].split(']')[0])
            value = int(i.split('= ')[1])
            for mask in possible_masks:
                add = find_addresses(address, mask)
                values[add] = value
    sum = 0
    for item in values:
        sum += values[item]
    print(sum)



def find_possible_masks(mask):
    finder = FindCombinations2()
    finder.find(mask)
    return finder.masks

def find_addresses(address, mask):
    binary_address = dec_to_bin(address)
    binary_string = '0'*(36-len(str(binary_address))) + str(binary_address)

    for i in range(len(mask)):
        if mask[i] == '0' or mask[i] == '1':
            binary_string = binary_string[:i] + mask[i] + binary_string[i+1:]

    return int(binary_string, 2)

class FindCombinations2:
    def __init__(self):
        self.masks = []

    def find(self, binary_string):
        X_location = []
        for index, i in enumerate(binary_string):
            if i == 'X':
                X_location.append(index)
        for i in itertools.product('01', repeat=len(X_location)):
            new_string = binary_string
            for k, j in enumerate(i):
                new_string = new_string[:X_location[k]] + j + new_string[X_location[k]+1:]
            self.masks.append(new_string)




class FindCombinations:

    def __init__(self):
        self.masks = []
    def find(self, binary_string):
        for i in range(len(binary_string)):
            if binary_string[i] == 'X':
                self.find(binary_string[:i] + '0' + binary_string[i+1:])
                self.find(binary_string[:i] + '1' + binary_string[i+1:])
        if 'X' not in binary_string and binary_string not in self.masks:
            self.masks.append(binary_string)
        return

#    return [int(add, 2) for add in addresses]



def apply_value(mask, address, value, values):
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