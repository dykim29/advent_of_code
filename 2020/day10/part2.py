from collections import defaultdict

def main():
    f = open("input_test.txt", "r")
    x = f.read().splitlines()
    x = [int(i) for i in x]
    x = sorted(x)
    # add my device which is 3 higher than highest
    x.append(x[-1]+3)
    x = [0] + x

    current_jolt = 0
    result = Solution(x).helper(current_jolt)
    print(result)

# Using memoization
class Solution:
    def __init__(self, x):
        self.cache = {}
        self.x = x

    def helper(self, current_jolt):
        if current_jolt == self.x[-1]:
            return 1
        if current_jolt not in self.x:
            return 0
        if current_jolt in self.cache:
            return self.cache[current_jolt]
        else:
            result = self.helper(current_jolt+1) + self.helper(current_jolt+2) + self.helper(current_jolt + 3)
            self.cache[current_jolt] = result
            return result





if __name__ == '__main__':
    main()