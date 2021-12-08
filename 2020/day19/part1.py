import re

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    split = x.index('')
    rules = rule_builder(x[:split])
    valid_messages = Messages(rules)
    valid_messages.find_message('0')

#    messages = message_builder(x[split+1:])
    messages = x[split+1:]
    print(len(set(messages).intersection(set(valid_messages.ls))))


def rule_builder(x):
    rules = {}
    for i in x:
        if "\"" in i:
            rules[i.split(":")[0]] = i.split("\"")[1]
        else:
            tmp = [elem.strip().split(' ') for elem in i.split(":")[1].split("|")]
            rules[i.split(":")[0]] = [elem for elem in tmp if elem != '']
    return rules


def message_builder(x):
    pass


class Messages:
    def __init__(self, rules):
        self.rules = rules
        self.ls = []

    def find_message(self, rule_no):
        for i in self.rules[rule_no]:
            self.helper('', i)


    def helper(self, string, stack):
        if not stack:
            self.ls.append(string)
            return
        if isinstance(self.rules[stack[0]], str):
            string = string + self.rules[stack[0]]
            stack.pop(0)
            self.helper(string, stack)
            return
        else:
            i = stack.pop(0)
            for elem in self.rules[i]:
                self.helper(string, elem + stack)
            return






if __name__ == '__main__':
    main()
