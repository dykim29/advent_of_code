def main():
    f = open("input.txt", "r")
    x = []
    for line in f.readlines():
        line = line.rstrip('\n')
        if line and x:
            x[-1] = x[-1] + ' ' + line
        elif line and not x:
            x.append(line)
        elif not line:
            x.append('')
    n_valid = 0
    for i in x:
        n_valid += check_valid_passport(i)
    print(n_valid)

def check_valid_passport(string):
    valid = (
            "byr:" in string and
            "iyr:" in string and
            "eyr:" in string and
            "hgt:" in string and
            "hcl:" in string and
            "ecl:" in string and
            "pid:" in string
#            "cid:" in string
            )
    return valid




if __name__ == '__main__':
    main()
