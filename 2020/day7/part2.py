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
            just_bags.append([int(re.search(r'\d', bag).group()), re.sub(r'\d ', '', bag)])

        graph[parent_bag] =just_bags
    n = count_bags(1, 'shiny gold', graph)
    print(n)

def count_bags(count, bag, graph):
    child_bags = {l[1]: l[0] for l in graph[bag]}
    print(child_bags)
    if not child_bags:
        print("RETURNING {}".format(count))
        return 0
    else:
        val=0
        for child_bag in child_bags:
            count = child_bags[child_bag]
            val += count * (1+count_bags(child_bags[child_bag], child_bag, graph))
        return val




if __name__ == '__main__':
    main()
