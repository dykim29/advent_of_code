from typing import List
from collections import defaultdict
import re


def parse_input(x):
    stacks = defaultdict(list)
    for idx, val in enumerate(x):
        if val == '':
            break_point = idx
            break
    stack_list = x[:break_point-1][::-1]
    instructions = x[break_point+1:]
    positions = x[break_point - 1]
    for idx, val in enumerate(positions):
        if val != ' ':
            for j in stack_list:
                try:
                    if j[idx]!= ' ':
                        stacks[val].append(j[idx])
                except IndexError:
                    pass
    instructions = [re.findall('[0-9]+', i) for i in instructions]
    return stacks, instructions



def part1(stacks, instructions: List[List[str]]):
    """
    Args:
        instructions: list of instructions, where one instruction is a list in the order [how_many_to_move, position_1,
         position_2]. e.g. ['1', '2', '3'] means move 1 from position 2 to position 3
    """
    for instruction in instructions:
        n = int(instruction[0])
        pos_before = instruction[1]
        pos_after = instruction[2]
        for i in range(n):
            stacks[pos_after].append(stacks[pos_before].pop())
    top_crates = [stacks[str(i)][-1] for i in range(1, len(stacks)+1)]
    return ''.join(top_crates)



def part2(stacks, instructions: List[List[str]]):
    for instruction in instructions:
        n = int(instruction[0])
        pos_before = instruction[1]
        pos_after = instruction[2]
        to_stack = []
        for i in range(n):
            to_stack.append(stacks[pos_before].pop())
        stacks[pos_after].extend(to_stack[::-1])
    top_crates = [stacks[str(i)][-1] for i in range(1, len(stacks)+1)]
    return ''.join(top_crates)

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    stacks, instructions = parse_input(x)
    print(part1(stacks.copy(), instructions))
    stacks, instructions = parse_input(x)
    print(part2(stacks.copy(), instructions))


if __name__ == '__main__':
    main()