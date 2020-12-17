from collections import defaultdict
import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    rules, my_ticket, nearby_tickets = clean_up_input(x)
    min_maxes = clean_up_rules(rules)
    cleaned_nearby_tickets = clean_up_nearby_tickets(nearby_tickets)
    print(cleaned_nearby_tickets)

    not_valid = []
    for i in cleaned_nearby_tickets:
        for no in i:
            if not check_valid(no, min_maxes):
                not_valid.append(no)
    print(sum(not_valid))

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

def clean_up_nearby_tickets(nearby_tickets):
    cleaned = []
    for i in nearby_tickets:
        t = i.split(',')
        cleaned.append([int(elem) for elem in t])
    return cleaned



if __name__ == '__main__':
    main()