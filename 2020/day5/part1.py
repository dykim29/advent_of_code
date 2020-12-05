def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    seat_ids = []
    for i in x:
        row = find_row(i[:7])
        col = find_col(i[7:])
        print(i, row, col)
        seat_ids.append(row * 8 + col)
    print(seat_ids)
    print(max(seat_ids))

def find_row(string):
    rows = list(range(0, 128))
    for i in string:
        if i == 'F':
            rows = rows[0:len(rows) / 2]
        else:
            rows = rows[len(rows) / 2:]
    assert len(rows) == 1
    return rows[0]

def find_col(string):
    cols = list(range(0, 8))
    for i in string:
        if i == 'L':
            cols = cols[0:len(cols) / 2]
        else:
            cols = cols[len(cols) / 2:]
    assert len(cols) == 1
    return cols[0]

if __name__ == '__main__':
    main()
