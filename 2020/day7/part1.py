import re
def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()

    graph = {}
    for i in x:
        parent_bag = i.split(' contain ')[0][:-5]
        latter_string = i.split(' contain ')[1]
        child_bags = re.findall(r'\d \w+ \w+', latter_string)
        just_bags = []
        for bag in child_bags:
            just_bags.append(re.sub(r'\d ', '', bag))

        graph[parent_bag] =just_bags
    # go through all parent bags recursively
    possible_parents = set()

    for bag in graph:
        found = find_shiny_gold_bag(bag, graph)
        #print(bag, found)
        if found:
            possible_parents.add(bag)
    print(possible_parents)
    print(len(possible_parents))

def find_shiny_gold_bag(bag, graph):
    child_bags = graph[bag]
    if 'shiny gold' in child_bags:
        return True
    elif not child_bags:
        return False
    else:
        val = 0
        for bag in child_bags:
            val += find_shiny_gold_bag(bag, graph)
        return val > 0


if __name__ == '__main__':
    main()
