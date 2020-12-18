from collections import defaultdict
import numpy as np


def main():
    f = open("input.txt", "r")
    input = f.read().splitlines()
    grid = {}
    for x, ls in enumerate(input):
        for y, elem in enumerate(ls):
            if elem == '#':
                grid[(x, y, 0)] = 1
    boundaries = [[0, len(input)-1], [0, len(input[0])-1], [0, 0]]

    cubes = Cubes(grid, boundaries)
#    for i in cubes.grid:
#        if i[2]==0:
#            print(i)
    for i in range(0,6):
        cubes.evolve()
    print(len(cubes.grid))


class Cubes:

    def __init__(self, grid, boundaries):
        self.grid = grid
        self.boundaries = boundaries

    def advance_boundaries(self):
        new_boundaries = []
        for i in self.boundaries:
            new_boundaries.append([i[0] - 1, i[1] + 1])
        self.boundaries = new_boundaries

    def evolve(self):
        self.advance_boundaries()
        self.grid_new = self.grid.copy()
        for x in range(self.boundaries[0][0], self.boundaries[0][1] + 1):
            for y in range(self.boundaries[1][0], self.boundaries[1][1] + 1):
                for z in range(self.boundaries[2][0], self.boundaries[2][1] + 1):
                    n_neighbours_active = self.find_number_of_active_neighbours(x,y,z)
                    if self.check_active(x,y,z) and not (n_neighbours_active == 2 or n_neighbours_active == 3):
                        self.grid_new.pop((x,y,z))
                    if not self.check_active(x,y,z) and n_neighbours_active == 3:
                        self.grid_new[(x,y,z)] = 1
        self.grid = self.grid_new

    def check_active(self, x, y, z):
        return bool(self.grid.get((x,y,z)))

    def find_number_of_active_neighbours(self, x, y, z):
        n_active = 0
        for x1 in range(x-1, x+2):
            for y1 in range(y - 1, y + 2):
                for z1 in range(z - 1, z + 2):
                    if not (x1 == x and y1 == y and z1==z):
                        n_active += self.check_active(x1, y1, z1)
        return n_active



if __name__ == '__main__':
    main()