
def solution(x: str, n_distinct: int):
    i = 0
    while len(set(x[i:i+n_distinct])) != n_distinct:
        i += 1
    return i + n_distinct


def main():
    f = open("input.txt", "r")
    x = f.readline()
    print(solution(x, 4))
    print(solution(x, 14))


if __name__ == '__main__':
    main()
