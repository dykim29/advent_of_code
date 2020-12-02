def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        x.append(int(line))
    for n1 in x:
        for n2 in x:
            if (2020-n1-n2) in x:
                print(n1, n2, 2020-n1-n2)
                print(n1*n2*(2020-n1-n2))

if __name__ == '__main__':
    main()
