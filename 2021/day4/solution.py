import numpy as np


def parse_input(x):
    drawn_numbers = [int(i) for i in x[0].split(',')]
    boards = []
    idx = 1
    while idx < len(x):
        if x[idx] == '':
            board = x[idx+1:idx+6].copy()
            board = [[int(j) for j in line.split()] for line in board]
        boards.append(np.array(board))
        idx += 6
    return drawn_numbers, boards


def part1(x):
    drawn_numbers, boards = parse_input(x)
    for idx in range(0, len(drawn_numbers)):
        for board_no, board in enumerate(boards):
            mask = np.isin(board, drawn_numbers[0:idx+1])
            winning_sum = is_winning_board(mask, board)
            if winning_sum:
                return winning_sum * drawn_numbers[idx]


def part2(x):
    drawn_numbers, boards = parse_input(x)
    board_list = list(range(len(boards)))
    for idx in range(0, len(drawn_numbers)):
        for board_no, board in enumerate(boards):
            mask = np.isin(board, drawn_numbers[0:idx+1])
            winning_sum = is_winning_board(mask, board)
            if winning_sum and board_no in board_list:
                board_list.remove(board_no)
            if len(board_list) == 0:
                return winning_sum * drawn_numbers[idx]


def is_winning_board(mask, board):
    """
    returns summ of all non-marked values if winning board.
    Returns false if not a winning board
    """
    vertical = mask.sum(axis=0)
    horizontal = mask.sum(axis=1)
    if len(np.where(horizontal == 5)[0]) > 0 or len(np.where(vertical == 5)[0]) > 0:
        return board[mask==False].sum()
    else:
        return False


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
    print(part2(x))


if __name__ == '__main__':
    main()