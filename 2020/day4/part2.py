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
        print(i)
        if check_valid_passport_fields_contained(i):
            print(check_every_field(i))
            n_valid += check_every_field(i)
    print(n_valid)

def check_valid_passport_fields_contained(string):
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

def check_every_field(string):
    validity = 1
    byr = string.split('byr:')[-1].split(' ')[0]
    iyr = string.split('iyr:')[-1].split(' ')[0]
    eyr = string.split('eyr:')[-1].split(' ')[0]
    hgt = string.split('hgt:')[-1].split(' ')[0]
    hcl = string.split('hcl:')[-1].split(' ')[0]
    ecl = string.split('ecl:')[-1].split(' ')[0]
    pid = string.split('pid:')[-1].split(' ')[0]

    validity = check_byr(byr) and check_iyr(iyr) and check_eyr(eyr) and check_hgt(hgt) and check_hcl(hcl) and check_ecl(ecl) and check_pid(pid)
    return validity



def check_byr(byr):
    return 1920 <= int(byr) <= 2002

def check_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def check_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def check_hgt(hgt):
    if hgt[-2:] == 'cm':
        height = int(hgt[:-2])
        return 150 <= height <= 193
    elif hgt[-2:] == 'in':
        height = int(hgt[:-2])
        return 59 <= height <= 76
    else:
        return False

def check_hcl(hcl):
    if hcl[0] == '#' and len(hcl)==7:
        for i in hcl[1:]:
            if i not in '0123456789abcdef':
                return False
    else:
        return False
    return True

def check_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(pid):
    return pid.isdigit() and len(pid) == 9


if __name__ == '__main__':

    main()
