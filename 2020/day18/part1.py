from collections import defaultdict
import numpy as np


def main():
    f = open("input.txt", "r")
    expressions = f.read().splitlines()
    for i, exp in enumerate(expressions):
        expressions[i] = [elem for elem in exp.replace(' ', '')]

    sum = 0
    for expression in expressions:
        sol = Solution(expression)
        print(sol.evaluate())
        sum += sol.evaluate()
    print(sum)


class Solution:

    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        ans = None
        while ans == None:
            ans = self.find_innermost_brackets()
        return ans

    def find_innermost_brackets(self):
        left =  None
        right = None
        for i, elem in enumerate(self.expression):
            if elem == '(':
                left = i
            elif elem == ')':
                right = i
                break
        if left is not None and right is not None:
            no = self.evaluate_inside_bracket(self.expression[left+1:right])
            self.expression = self.expression[0:left] + [str(no)] + self.expression[right+1:]
        else:
            no = self.evaluate_inside_bracket(self.expression)
            return no

    def evaluate_inside_bracket(self, to_eval):
        map = {
            '+': np.add,
            '*': np.multiply
        }
        val = int(to_eval[0])
        left = to_eval[1:]
        while left:
            val = map[left[0]](val, int(left[1]))
            left = left[2:]
        return val


if __name__ == '__main__':
    main()