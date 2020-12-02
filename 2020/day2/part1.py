def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        x.append(line[:-1])

    n_valid = 0
    for i in x:
        min = int(i.split('-')[0])
        max = int(i.split('-')[1].split(' ')[0])
        letter = i.split(':')[0][-1]
        password = i.split(': ')[-1]
        counts = password.count(letter)
        if min <= counts <= max:
            print(min, counts, max, i)
            n_valid += 1

    print(n_valid)

if __name__ == '__main__':
    main()
