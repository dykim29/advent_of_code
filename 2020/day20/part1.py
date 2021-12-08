import numpy as np

def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    tiles = tile_builder(x)
    tile_edges = {}
    for tile_no, grid in tiles.items():
        tile_edges[tile_no] = [grid[0,:], grid[-1, :], grid[:,0], grid[:,-1]]
    tile_edge_matched = {}
    for tile_no in tile_edges:
        n_found = 0
        for edge in tile_edges[tile_no]:
            n_found += find_edge_match(tile_no, edge, tile_edges)
        tile_edge_matched[tile_no] = n_found
    print(tile_edge_matched)
    multiple = 1
    for tile_no in tile_edge_matched:
        if tile_edge_matched[tile_no] == 2:
            print(tile_no, multiple)
            multiple = multiple * int(tile_no)
    print(multiple)


def find_edge_match(tile_no, edge, tile_edges):
    for tile_no2 in tile_edges:
        if tile_no != tile_no2:
            for edge2 in tile_edges[tile_no2]:
                if (edge == edge2).all() or (edge[::-1] == edge2).all():
                    return True
    return False








def tile_builder(x):
    tiles = [[]]
    for i, j in enumerate(x):
        if j == "":
            tiles.append([])
        else:
            tiles[-1].append(j)
    tile_objects = {}
    for tile in tiles:
        tile_no = tile[0].split("Tile ")[1].split(':')[0]
        grid = tile[1:]
        for i in range(len(grid)):
            grid[i] = [elem for elem in grid[i]]
        grid = np.array(grid)
        tile_objects[tile_no] = grid

    return tile_objects


if __name__ == '__main__':
    main()
