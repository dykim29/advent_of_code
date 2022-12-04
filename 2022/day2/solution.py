
def part1(x):
    selection_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    def get_round_win(opponent, me):
        if opponent == 'A' and me == 'X':
            return 'tie'
        elif opponent == 'A' and me == 'Y':
            return 'win'
        elif opponent == 'A' and me == 'Z':
            return 'lose'
        elif opponent == 'B' and me == 'X':
            return 'lose'
        elif opponent == 'B' and me == 'Y':
            return 'tie'
        elif opponent == 'B' and me == 'Z':
            return 'win'
        elif opponent == 'C' and me == 'X':
            return 'win'
        elif opponent == 'C' and me == 'Y':
            return 'lose'
        elif opponent == 'C' and me == 'Z':
            return 'tie'

    total_score = 0
    for i in x:
        opponent = i[0]
        me = i[-1]
        selection_score = selection_scores[me]
        round_result = get_round_win(opponent, me)
        if round_result == 'lose':
            round_score = 0
        elif round_result == 'tie':
            round_score = 3
        elif round_result=='win':
            round_score = 6
        total_score  += selection_score + round_score
    return total_score



def part2(x):
    selection_scores = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    def get_round_win(opponent, me):
        if opponent == 'A' and me == 'X':
            return 3
        elif opponent == 'A' and me == 'Y':
            return 1
        elif opponent == 'A' and me == 'Z':
            return 2
        elif opponent == 'B' and me == 'X':
            return 1
        elif opponent == 'B' and me == 'Y':
            return 2
        elif opponent == 'B' and me == 'Z':
            return 3
        elif opponent == 'C' and me == 'X':
            return 2
        elif opponent == 'C' and me == 'Y':
            return 3
        elif opponent == 'C' and me == 'Z':
            return 1

    total_score = 0
    for i in x:
        opponent = i[0]
        me = i[-1]
        selection_score = selection_scores[me]
        round_score = get_round_win(opponent, me)
        total_score += selection_score + round_score
    return total_score


def main():

    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()