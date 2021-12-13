import numpy as np

def parse_input(x):
    blank_line_idx = x.index("")
    x_values = []
    y_values = []
    for i in range(blank_line_idx):
        x_values.append(int(x[i].split(',')[0]))
        y_values.append(int(x[i].split(',')[1]))
    paper = np.zeros((max(x_values) + 1, max(y_values) + 1))
    for i in range(len(x_values)):
        paper[x_values[i], y_values[i]] = 1

    folds = []
    for i in range(blank_line_idx + 1, len(x)):
        folds.append([x[i].split('=')[0][-1], int(x[i].split('=')[1])])
    return paper, folds


def solution(paper, folds):
    for idx, fold in enumerate(folds):
        if fold[0] == 'x':
            up = paper[0:fold[1], :]
            down = paper[fold[1]+1:, :]
            if up.shape[0] > down.shape[0]:
                down = np.concatenate((down, np.zeros((up.shape[0] - down.shape[0], down.shape[1]))), axis=0)
            elif up.shape[0] < down.shape[0]:
                up = np.concatenate((np.zeros((down.shape[0] - up.shape[0], down.shape[1])), up), axis=0)
            paper = np.logical_or(up, down[::-1, :]).astype(int)
        elif fold[0] == 'y':
            left = paper[:, 0:fold[1]]
            right = paper[:, fold[1]+1:]
            if left.shape[1] > right.shape[1]:
                right = np.concatenate((right, np.zeros((left.shape[0], left.shape[1] - right.shape[1]))), axis=1)
            elif left.shape[1] < right.shape[1]:
                left = np.concatenate((np.zeros((left.shape[0],  right.shape[1] - left.shape[1])), left), axis=1)
            paper = np.logical_or(left, right[:, ::-1]).astype(int)
        if idx == 0:
            print('PART 1 ANSWER:', np.count_nonzero(paper))

    # For easier visualisation:
    paper = paper.astype(str)
    paper[paper == '0'] = '.'
    paper[paper == '1'] = '⬤'
    print(paper.T[:, :14])
    print(paper.T[:, 14:25])
    print(paper.T[:, 25:])


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    paper, folds = parse_input(x)
    print(solution(paper, folds))


if __name__ == '__main__':
    main()
