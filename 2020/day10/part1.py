from collections import defaultdict

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = [int(i) for i in x]
    x = sorted(x)
    # add my device which is 3 higher than highest
    x.append(x[-1]+3)

    start = 0
    diffs = defaultdict(int)
    for i in x:
        diffs[i - start] +=1
        start = i
    print(diffs)
    print(diffs[1] * diffs[3])



if __name__ == '__main__':
    main()