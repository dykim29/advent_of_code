from collections import defaultdict

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    split = x.index('')
    rules = rule_builder(x[:split])
    messages = x[split+1:]
    max_length_message = len(max(messages, key=len))
    # replace rules for 8 and 11:
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]

    set_message = build_sets(messages, max_length_message)
    valid_messages = Messages(rules, set_message)
    valid_messages.find_message('0')
#
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


def build_sets(messages, max_length_message):
    dict_message = defaultdict(set)
    for i in range(0, max_length_message+1):
        for message in messages:
            if i <= len(message):
                dict_message[i].add(message[:i])
    return dict_message



class Messages:
    def __init__(self, rules,  set_message):
        self.rules = rules
        self.set_message = set_message
        self.ls = []

    def find_message(self, rule_no):
        for i in self.rules[rule_no]:
            self.helper('', i, [])


    def helper(self, string, stack, hist):
        if string not in self.set_message[len(string)]:
            #print('abandon', string, stack, hist)
            return None
        if not stack:
            self.ls.append(string)
            return string
        if isinstance(self.rules[stack[0]], str):
            string = string + self.rules[stack[0]]
            a = stack.pop(0)
            hist.append(a)
            self.helper(string, stack, hist)
            return
        else:
            i = stack.pop(0)
            for elem in self.rules[i]:
                self.helper(string, elem + stack, hist)
            return






if __name__ == '__main__':
    main()
