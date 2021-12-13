class Cave:
    def __init__(self, name):
        self.name = name
        self.adj = []
        if self.name.isupper():
            self.type = 'big'
        else:
            self.type = 'small'

    def __repr__(self):
        return self.name

    def add_edge(self, cave2):
        self.adj.append(cave2)


class Graph:
    def __init__(self):
        self.caves = {}

    def add_cave(self, cave_name):
        cave = Cave(cave_name)
        self.caves[cave_name] = cave

    def add_edge_between_caves(self, cave1:Cave, cave2:Cave):
        cave1.add_edge(cave2)
        cave2.add_edge(cave1)


def create_graph(x):
    graph = Graph()
    for i in x:
        cave1, cave2 = i.split('-')
        if cave1 not in graph.caves:
            graph.add_cave(cave1)
        if cave2 not in graph.caves:
            graph.add_cave(cave2)
        graph.add_edge_between_caves(graph.caves[cave1], graph.caves[cave2])
    return graph


def part1(x):
    graph = create_graph(x)
    return count_paths(graph)


def count_paths(graph):
   starting_cave = graph.caves['start']
   visited = {cave_name: False for cave_name in graph.caves}
   path_count = [0]
   path = []
   helper(starting_cave, 'end', path_count, visited, path)
   return path_count


def helper(cave: Cave, end_destination_cave_name, path_count, visited_caves, path):
    print(cave, end_destination_cave_name, path_count, visited_caves, path)
    visited_caves[cave.name] = True
    path.append(cave.name)
    if cave.name == end_destination_cave_name:
        print('REACHED END', path)
        path.pop()
        path_count[0] += 1
        visited_caves[cave.name] = False
        return
    else:
        for i in cave.adj:
            if not (visited_caves[i.name] == True and i.type == 'small'):
                helper(i, end_destination_cave_name, path_count, visited_caves, path)
    visited_caves[cave.name] = False
    path.pop()


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    print(part1(x))
   # print(part2(x))


if __name__ == '__main__':
    main()
