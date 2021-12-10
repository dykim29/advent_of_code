bracket_dict = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}


def part1(x):
    char_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    total = 0
    for line in x:
        char = is_line_corrupt(line)
        if char:
            total += char_points[char]
    return total


def is_line_corrupt(line):
    """
    :param line: list e.g. ['[', '(', '{', '(', '<', '(', '(', ')', ')']
    """
    stack = []
    for char in line:
        if char in bracket_dict.keys():
            stack.append(char)
        else:
            last_opening = stack.pop()
            if bracket_dict[last_opening] != char:
                return char
    return False


def part2(x):
    scores = []
    for line in x:
        if not is_line_corrupt(line):
            autocomplete = get_line_completion(line)
            scores.append(calculate_points(autocomplete))
    return sorted(scores)[len(scores)//2]


def get_line_completion(line):
    stack = []
    queue = line
    while queue:
        char = queue.pop(0)
        if char in bracket_dict.keys():
            stack.append(char)
        else:
            stack.pop()
    # Now build autocomplete section
    autocomplete = []
    while stack:
        autocomplete.append(bracket_dict[stack.pop()])
    return autocomplete


def calculate_points(autocomplete):
    char_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for i in autocomplete:
        score = score*5 + char_points[i]
    return score


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = [[i for i in string] for string in x]
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()
