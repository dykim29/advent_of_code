def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    y = [[]]
    for i in x:
        if i:
            y[-1] = y[-1] + [i]
        else:
            y.append([])
    sum = 0
    for i in y:
        set_q = set(i[0])
        for j in i:
            set_q = set_q.intersection(set(j))
        print(len(set_q))
        sum += len(set_q)
    print(sum)


if __name__ == '__main__':
    main()
