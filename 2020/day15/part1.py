# slow solution
from collections import defaultdict
import numpy as np


def main():
    # Starting numbers
    #solution = Solution([0,3,6])
    solution = Solution([17,1,3,16,19,0])
    for i in range(30000000):
        if i % 10000 == 0:
            print('done with', i)
        solution.find_next_number()
    print(solution.x[30000000-1])

class Solution:
    def __init__(self, starting_numbers):
        self.x = starting_numbers
        self.no_of_times_spoken = defaultdict(int)

        for i in self.x:
            self.no_of_times_spoken[i] += 1

    def find_next_number(self):
        last_spoken = self.x[-1]
        if self.no_of_times_spoken[last_spoken] == 1:
            self.x.append(0)
            self.no_of_times_spoken[0] += 1
        else:
            count = 0
            for i in self.x[-2::-1]:
                count += 1
                if i == last_spoken:
                    break
            self.x.append(count)
            self.no_of_times_spoken[count] += 1


if __name__ == '__main__':
    main()