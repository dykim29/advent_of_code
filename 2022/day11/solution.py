from __future__ import annotations
from typing import List
import re


class Monkey:
    def __init__(self, items: list, test_div_condition: int, operation, action_on_true, action_on_false,
                 relief: bool):
        """
        operation: e.g. ["*", '19'] to indicate new = old * 19.
        """
        self.items = items
        self.test_div_condition = test_div_condition
        self.action_on_true = action_on_true
        self.action_on_false = action_on_false
        self.operation = operation
        self.n_inspects = 0
        self.relief = relief

    def test_cond(self, item: int):
        return item % self.test_div_condition == 0

    def operate(self, val):
        if self.operation[0] == "*":
            if self.operation[1].isdigit():
                return val * int(self.operation[1])
            elif self.operation[1] == 'old':
                return val * val
            else:
                raise ValueError(f"Invalid operation, {self.operation}")
        elif self.operation[0] == "+":
            return val + int(self.operation[1])
        else:
            raise ValueError(f"Invalid operation, {self.operation}")

    def play(self, monkeys: List[Monkey], least_common_multiple):
        for i in range(len(self.items)):
            item = self.items.pop(0)
            item = self.operate(item)
            if self.relief:
                item = item // 3
            self.n_inspects += 1
            item = item % least_common_multiple
            if self.test_cond(item):
                monkeys[self.action_on_true].items.append(item)
            else:
                monkeys[self.action_on_false].items.append(item)


def parse_input(x, relief: bool):
    chunk_size = 7
    instructions = list(split(x, chunk_size))
    monkeys = []
    lcm = 1
    for i in instructions:
        starting_items = [int(i) for i in re.findall('[0-9]+', i[1])]
        operation = i[2].split(' ')[-2:]
        test_div_condition = int(re.findall('[0-9]+', i[3])[0])
        action_on_true = int(re.findall('[0-9]+', i[4])[0])
        action_on_false = int(re.findall('[0-9]+', i[5])[0])
        lcm *= test_div_condition
        monkeys.append(Monkey(starting_items, test_div_condition, operation, action_on_true, action_on_false, relief))

    return monkeys, lcm


def split(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


def part1(x):
    monkeys, lcm = parse_input(x, True)
    for i in range(20):
        for monkey in monkeys:
            monkey.play(monkeys, lcm)

    n_inspects = []
    for monkey in monkeys:
        n_inspects.append(monkey.n_inspects)
    sorted_list = sorted(n_inspects)
    return sorted_list[-2] * sorted_list[-1]


def part2(x):
    monkeys, lcm = parse_input(x, False)
    for i in range(10000):
        for idx, monkey in enumerate(monkeys):
            monkey.play(monkeys, lcm)

    n_inspects = []
    for monkey in monkeys:
        n_inspects.append(monkey.n_inspects)
    sorted_list = sorted(n_inspects)
    return sorted_list[-2] * sorted_list[-1]


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()