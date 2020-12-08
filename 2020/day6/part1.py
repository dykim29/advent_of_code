def main():
    f = open("input_test.txt", "r")
    x = f.read().splitlines()

    y = ['']
    for i in x:
        if i:
            y[-1] = y[-1] + i
        else:
            y.append(i)

    sum = 0
    for i in y:
        print(len(set(i)))
        sum += len(set(i))
    print(sum)

if __name__ == '__main__':
    main()
