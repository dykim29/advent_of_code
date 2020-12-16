import numpy as np
# Same solution but much faster

def main():
    # Starting numbers

    starting_solutions =[17,1,3,16,19,0] #[0,3,6]
#    solution = Solution([0,3,6])
    solution = Solution(starting_solutions)
    counter = len(starting_solutions)
    for i in range(30000000):
        if i % 10000 == 0:
            print('done with', i)
        solution.find_next_number()
        counter += 1
        if counter == 30000000:
            print(solution.last_spoken)

class Solution:
    def __init__(self, starting_numbers):
        self.x = starting_numbers
        self.when_last_spoken = {}

        for index, i in enumerate(self.x[:-1]):
            self.when_last_spoken[i] = index
        self.last_spoken = self.x[-1]
        self.count = len(self.x)-1

    def find_next_number(self):

        if self.when_last_spoken.get(self.last_spoken) == None:
            self.when_last_spoken[self.last_spoken] = self.count
            self.last_spoken = 0
            self.count += 1
        else:
            old_last_spoken = self.last_spoken
            self.last_spoken = self.count - self.when_last_spoken[self.last_spoken]
            self.when_last_spoken[old_last_spoken] = self.count
            self.count += 1


if __name__ == '__main__':
    main()