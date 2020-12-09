import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = [int(y) for y in x]

    preamble_size = 25
    problematic_elem, i = find_error(preamble_size, x)
    print(problematic_elem, i)
    fi, li = find_contiguous(problematic_elem, x)
    print(fi, li)
    print(np.sum(x[fi:li]))
    print('Sum of smallest and largest:')
    print(min(x[fi:li]) + max(x[fi:li]))


def find_contiguous(k, x):
    # find subarray in x which sum to k
    first_index = 0
    last_index = 0
    sum = 0
    while sum != k:
        if sum < k:
            last_index +=1
            sum += x[last_index-1]
        elif sum > k:
            first_index +=1
            sum -= x[first_index-1]
        else:
            pass
    return first_index, last_index



def find_error(preamble_size, x):
    for i, y in enumerate(x):
        if i < preamble_size:
            continue
        elem = y
        found = 0
        for el1 in x[i-preamble_size:i]:
            if elem - el1 in x[i-preamble_size:i]:
                found = 1
        if found == 0:
            return elem, i


if __name__ == '__main__':
    main()