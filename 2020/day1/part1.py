def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        x.append(int(line))

    for n in x:
        if (2020 - n) in x:
            print(n, 2020-n)
            print(n * (2020-n))
            return


if __name__ == '__main__':
    main()
