def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        x.append(line[:-1])

    n_valid = 0
    for i in x:
        pos1 = int(i.split('-')[0])
        pos2 = int(i.split('-')[1].split(' ')[0])
        letter = i.split(':')[0][-1]
        password = i.split(': ')[-1]
        valid = (password[pos1-1] == letter) + (password[pos2-1] == letter) == 1
        print(i, valid)
        if valid:
            n_valid += 1

    print(n_valid)

if __name__ == '__main__':
    main()
