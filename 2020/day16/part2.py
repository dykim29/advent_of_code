from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    rules, my_ticket, nearby_tickets = clean_up_input(x)
    my_ticket = [int(elem) for elem in my_ticket[0].split(',')]
    min_maxes = clean_up_rules(rules)
    cleaned_nearby_tickets = clean_up_nearby_tickets(nearby_tickets)
    print(cleaned_nearby_tickets)

# now obtain the valid tickets only
    cleaned_valid_tickets = cleaned_nearby_tickets[:]
    for i in cleaned_nearby_tickets:
        for no in i:
            if not check_valid(no, min_maxes):
                cleaned_valid_tickets.remove(i)

    possible_headers = {}
    better_min_maxes = clean_up_rules2(rules)
    cleaned_valid_tickets = np.array(cleaned_valid_tickets)
    rows, cols = cleaned_valid_tickets.shape
    for col in range(cols):
        for row in range(rows):
            possible_rules = set()
            no = cleaned_valid_tickets[row, col]
            for rule_index, rule in enumerate(better_min_maxes):
                if rule[0][0] <= no <= rule[0][1] or rule[1][0] <= no <= rule[1][1]:
                    possible_rules.add(rule_index)
            if possible_headers.get(col):
                possible_headers[col] = possible_headers[col].intersection(set(possible_rules))
            else:
                possible_headers[col] = set(possible_rules)

    stand_alone = []
    while not finished(possible_headers):
        for i in possible_headers:
            if i not in stand_alone:
                if len(possible_headers[i]) == 1:
                    narrowed = list(possible_headers[i])[0]
                    col = i
                    stand_alone.append(col)
        for i in possible_headers:
            if i != col:
                possible_headers[i].discard(narrowed)
        print(stand_alone)
    print(possible_headers)

    it = []
    for i in possible_headers:
        if list(possible_headers[i])[0] in [0,1,2,3,4,5]:
            it.append(i)
    print(it)
    multiple = 1
    for i in it:
        multiple *= my_ticket[i]
    print(multiple)


def finished(possible_headers):
    for i in possible_headers:
        if len(possible_headers[i]) != 1:
            return False
    return True




def check_valid(no, min_maxes):
    for rule in min_maxes:
        if rule[0] <= no <= rule[1]:
            return True
    return False

def clean_up_input(x):
    #rules = x[:3]
    #my_ticket = x[5:6]
    #nearby_tickets = x[8:]
    rules = x[:20]
    my_ticket = x[22:23]
    nearby_tickets = x[25:]
    return rules, my_ticket, nearby_tickets

def clean_up_rules(rules):
    min_maxes = []
    for rule in rules:
        rule_name = rule.split(':')[0]
        min1 = int(rule.split(': ')[1].split(' or ')[0].split('-')[0])
        max1 = int(rule.split(': ')[1].split(' or ')[0].split('-')[1])
        min2 = int(rule.split(' or ')[1].split('-')[0])
        max2 = int(rule.split(' or ')[1].split('-')[1])
        min_maxes.append([min1, max1])
        min_maxes.append([min2, max2])
    return min_maxes

def clean_up_rules2(rules):
    min_maxes = []
    for rule in rules:
        rule_name = rule.split(':')[0]
        min1 = int(rule.split(': ')[1].split(' or ')[0].split('-')[0])
        max1 = int(rule.split(': ')[1].split(' or ')[0].split('-')[1])
        min2 = int(rule.split(' or ')[1].split('-')[0])
        max2 = int(rule.split(' or ')[1].split('-')[1])
        min_maxes.append([[min1, max1], [min2, max2]])
    return min_maxes


def clean_up_nearby_tickets(nearby_tickets):
    cleaned = []
    for i in nearby_tickets:
        t = i.split(',')
        cleaned.append([int(elem) for elem in t])
    return cleaned



if __name__ == '__main__':
    main()