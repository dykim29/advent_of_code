import numpy as np
from queue import PriorityQueue


def parse_input(x):
    y = []
    for i in x:
        y.append([int(j) for j in i])
    return np.array(y).astype(int)

def part1(x):
    visited = set()
    positions = {(i, j) for i in range(x.shape[0]) for j in range(x.shape[1])}
    start_position = (0, 0)
    D = dijkstra(positions, start_position, visited, x)
    return D[(x.shape[0]-1, x.shape[1]-1)]


def find_valid_neighbours(current_position, grid):
    x, y = current_position
    candidate_positions = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    neighbours = []
    for x,y in candidate_positions:
        if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
            neighbours.append((x,y))
    return neighbours


def dijkstra(positions, start_position, visited, x):
    """ Uses the Dijkstra algorithm to find the shorted path in a weighted graph https://stackabuse.com/dijkstras-algorithm-in-python/"""
    D = {v: float('inf') for v in positions}
    D[start_position] = 0

    pq = PriorityQueue()
    pq.put((0, start_position))

    while not pq.empty():
        (dist, current_position) = pq.get()
        visited.add(current_position)

        for neighbor in find_valid_neighbours(current_position, x):
            distance = x[neighbor]
            if neighbor not in visited:
                old_cost = D[neighbor]
                new_cost = D[current_position] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D

def part2(x):
    big_grid = create_big_grid(x)
    visited = set()
    positions = {(i, j) for i in range(big_grid.shape[0]) for j in range(big_grid.shape[1])}
    start_position = (0, 0)
    D = dijkstra(positions, start_position, visited, big_grid)
    return D[(big_grid.shape[0]-1, big_grid.shape[1]-1)]

def create_big_grid(small_grid):
    x, y = small_grid.shape
    big_grid = np.zeros((x*5, y*5))
    for x_step in range(0, 5):
        for y_step in range(0, 5):
            big_grid[x_step*x : x_step*x + x, y_step * y: y_step *y + y] = create_new_grid(x_step + y_step, small_grid)
    return big_grid

def create_new_grid(stepsize, x):
    # stepsize is number of steps away from x - whether it's downward or to the right
    y = x + stepsize
    y[y > 9] = y[y>9] - 9
    return y



def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    x = parse_input(x)
    print(part1(x))
    print(part2(x))



if __name__ == '__main__':
    main()
