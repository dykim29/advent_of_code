from collections import Counter

class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.next = None

    def __repr__(self):
        return self.dataval


def parse_input(x):

    polymer_template = x[0]
    polymer_rules = {}
    for i in x[2:]:
        key, val = i.split(' -> ')
        polymer_rules[key] = val

    # Create linked list.
    head = Node(polymer_template[0])
    current = head
    for i in polymer_template[1:]:
        next = Node(i)
        current.next = next
        current = next
    return head, polymer_rules, polymer_template


def get_linked_list_values(head: Node):
    listvals = []
    current = head
    while current is not None:
        listvals.append(current.dataval)
        current = current.next
    return listvals


def part1(head, polymer_rules):
    """
    This solution uses linked list. It's too slow to do part 2
    """
    for i in range(10):
        current = head
        while current.next is not None:
            next_node = current.next
            pair = ''.join([current.dataval, next_node.dataval])
            val_to_insert = polymer_rules[pair]
            new_node = Node(val_to_insert)
            current.next = new_node
            new_node.next = next_node

            current = next_node
    ls = get_linked_list_values(head)
    counter = Counter(ls)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


def part2(polymer_template: str, polymer_rules: dict, no_of_steps):
    """
    Keep track of counts of each pair that exist, rather than the entire linked list.
    """
    pairs = convert_template_to_pairs(polymer_template)
    for i in range(no_of_steps):
        new_pairs = pairs.copy()
        for pair in pairs:
            old_val = pairs[pair]
            char_to_insert = polymer_rules[pair]
            new_beg_pair = pair[0] + char_to_insert
            new_latter_pair = char_to_insert + pair[1]
            new_pairs[pair] -= old_val
            new_pairs[new_beg_pair] += old_val
            new_pairs[new_latter_pair] += old_val
        pairs = new_pairs
    letter_count = convert_pairs_to_letter_counts(pairs, polymer_template)
    return int(letter_count.most_common()[0][1] - letter_count.most_common()[-1][1])



def convert_pairs_to_letter_counts(pairs, starting_template):
    letter_count = Counter()
    for pair in pairs:
        letter_count[pair[0]] += pairs[pair]
        letter_count[pair[1]] += pairs[pair]
    # This means all letters are counted twice EXCEPT for the beginning letter and ending letter, which is counted 1 less than twice
    for i in letter_count:
        if i == starting_template[0] or i == starting_template[-1]:
            letter_count[i] = (letter_count[i]+1)/2
        else:
            letter_count[i] = letter_count[i] / 2
    return letter_count

def convert_template_to_pairs(polymer_template):
    pairs = Counter()
    for idx in range(len(polymer_template) - 1):
        pair = polymer_template[idx] + polymer_template[idx + 1]
        pairs[pair] += 1
    return pairs

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    head, polymer_rules, polymer_template = parse_input(x)
    get_linked_list_values(head)
    print(part1(head, polymer_rules))
    print(part2(polymer_template, polymer_rules, 40))



if __name__ == '__main__':
    main()
