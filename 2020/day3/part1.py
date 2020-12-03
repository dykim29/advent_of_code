def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    pos = 0
    tree_count = 0
    for i in x:
        print(i, pos, len(i))
        if i[pos] == '#':
            tree_count += 1
        pos = (pos + 3) % len(i)

    print(tree_count)

if __name__ == '__main__':
    main()
