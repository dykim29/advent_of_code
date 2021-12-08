import numpy as np

def main():
    f = open("input_test.txt", "r")
    x = f.read().splitlines()
    tiles = Tiles(tile_builder(x))
    tile_no = list(tiles.tiles_dict.keys())[0]
    tiles.fixed_tiles.add(tile_no)
    tiles.tiles_to_match.add(tile_no)

    while tiles.tiles_to_match:
#    for tile_no in tiles.tiles_dict:
        tiles.find_match(tile_no)
    for tile_no in tiles.tiles_dict:
        print(tile_no, )
        if tiles.tiles_dict[tile_no].top_match:
            print('top',tiles.tiles_dict[tile_no].top_match.tile_no)
        if tiles.tiles_dict[tile_no].right_match:
            print('right',tiles.tiles_dict[tile_no].right_match.tile_no)
        if tiles.tiles_dict[tile_no].left_match:
            print('left',tiles.tiles_dict[tile_no].left_match.tile_no)
        if tiles.tiles_dict[tile_no].bottom_match:
            print('bottom',tiles.tiles_dict[tile_no].bottom_match.tile_no)

class Tiles:

    def __init__(self, tiles):
        self.tiles_dict = tiles
        self.fixed_tiles = set()
        self.tiles_to_match = set()

    def find_match(self, tile_no):
        tile = self.tiles_dict[tile_no]
        for key, other_tile in self.tiles_dict.items():
            if key == tile_no:
                continue
            transformations = [other_tile.rotate, other_tile.rotate, other_tile.rotate, other_tile.flip, other_tile.rotate, other_tile.rotate, other_tile.rotate]
            matched = self.find_match_fixed_orientation(tile, other_tile)
            if not matched and other_tile not in self.fixed_tiles:
                for transformation in transformations:
                    transformation()
                    matched = self.find_match_fixed_orientation(tile, other_tile)
                    if matched:
                        break


    def find_match_fixed_orientation(self, tile1, tile2):
        matched =  False
        if (tile1.bottom == tile2.top).all():
            tile1.bottom_match = tile2
            tile2.top_match = tile1
            self.fixed_tiles.add(tile2.tile_no)
            matched=True
        if (tile1.top == tile2.bottom).all():
            tile1.top_match = tile2
            tile2.bottom_match = tile1
            self.fixed_tiles.add(tile2.tile_no)
            matched=True
        if (tile1.left == tile2.right).all():
            tile1.left_match = tile2
            tile2.right_match = tile1
            self.fixed_tiles.add(tile2.tile_no)
            matched=True
        if (tile1.right == tile2.left).all():
            tile1.right_match = tile2
            tile2.left_match = tile1
            self.fixed_tiles.add(tile2.tile_no)
            matched=True
        return matched


class Tile:
    def __init__(self, tile_no, grid):
        self.tile_no = tile_no
        self.grid = grid
        self.define_edges()
        self.top_match = None
        self.bottom_match = None
        self.left_match = None
        self.right_match = None

    def define_edges(self):
        self.top = self.grid[0,:]
        self.bottom = self.grid[-1,:]
        self.left = self.grid[:,0]
        self.right = self.grid[:,-1]

    def rotate(self):
        self.grid = np.rot90(self.grid)
        self.define_edges()

    def flip(self):
        self.grid = np.fliplr(self.grid)
        self.define_edges()


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
        tile_objects[tile_no] = Tile(tile_no, grid)

    return tile_objects





if __name__ == '__main__':
    main()
