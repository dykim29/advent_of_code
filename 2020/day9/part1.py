
def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    preamble_size = 25
    elem = find_error(preamble_size, x)
    print(elem)



def find_error(preamble_size, x):
    for i, y in enumerate(x):
        if i < preamble_size:
            continue
        elem = y
        found = 0
        for el1 in x[i-preamble_size:i]:
            if str(int(elem) - int(el1) ) in x[i-preamble_size:i]:
                found = 1
        if found == 0:
            return elem


if __name__ == '__main__':
    main()