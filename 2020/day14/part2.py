from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    values = {}
#    print(find_addresses(42, '000000X000X00X000000000X000000X1001X'))
    for index, i in enumerate(x):
        print('doing line number {}'.format(index))
        if i[0:4] == 'mask':
            mask = [elem for elem in i[7:]]
        else:
            address = int(i.split('[')[1].split(']')[0])
            value = int(i.split('= ')[1])
            addresses_to_alter = find_addresses(address, mask)
            for add in addresses_to_alter:
                values[add] = value
    sum = 0
    for item in values:
        sum += values[item]
    print(sum)
#

def find_addresses(address, mask):
    binary_address = dec_to_bin(address)
    binary_string = '0'*(36-len(str(binary_address))) + str(binary_address)

    for i in range(len(mask)):
        if mask[i] != '0':
            binary_string = binary_string[:i] + mask[i] + binary_string[i+1:]

    finder = FindCombinations()
    finder.find(binary_string)

    return [int(add, 2) for add in finder.addresses]


class FindCombinations:

    def __init__(self):
        self.addresses = []
    def find(self, binary_string):
        for i in range(len(binary_string)):
            if binary_string[i] == 'X':
                self.find(binary_string[:i] + '0' + binary_string[i+1:])
                self.find(binary_string[:i] + '1' + binary_string[i+1:])
        if 'X' not in binary_string and binary_string not in self.addresses:
            self.addresses.append(binary_string)
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