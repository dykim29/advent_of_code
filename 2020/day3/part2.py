def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    pos = 0
    multiplied = count_trees(1, 1, x) * count_trees(3, 1, x) * count_trees(5, 1, x) * count_trees(7, 1, x) * count_trees(1, 2, x)
    print(multiplied)

def count_trees(right, down, x):
    tree_count = 0
    pos=0
    for i in x:
        if i[pos] == '#':
            tree_count += 1
        pos = (pos + right) % len(i)
    tree_count = 0
    pos = 0
    for i in x[::down]:
        if i[pos] == '#':
            tree_count += 1
        pos = (pos + right) % len(i)
    return tree_count

if __name__ == '__main__':
    main()
