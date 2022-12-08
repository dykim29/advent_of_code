from __future__ import annotations
from typing import List

import numpy as np

class File:
    """
    If size is None, is a directory; otherwise file.
    """
    def __init__(self, name: str, parent_dir: File | None, size=None):
        self.name = name
        self.parent_dir = parent_dir
        self.size = size
        self.contents = []

    def __repr__(self):
        return f"File ({self.name})"

    def add_content(self, file: File):
        self.contents.append(file)


def parse_input(x):
    home = File('/', None)
    current_dir = home
    list_of_all_dirs = [home]

    for i in x[1:]:
        if i[:4] == "$ cd":
            if i.split("$ cd ")[-1] == '..':
                current_dir = current_dir.parent_dir
            else:
                dir_name = i.split("$ cd ")[-1]
                for content in current_dir.contents:
                    if content.name == dir_name:
                        current_dir = content
        elif i == "$ ls":
            pass
        elif i.split(' ')[0] == 'dir':
            dir_name = i.split(" ")[-1]
            new_dir = File(dir_name, current_dir)
            list_of_all_dirs.append(new_dir)
            current_dir.add_content(new_dir)
        elif i.split(' ')[0].isdigit() :
            file_name = i.split(" ")[-1]
            current_dir.add_content(File(file_name, current_dir, size=int(i.split(" ")[0])))
        else:
            raise ValueError(f"Unrecognised command type, {i}")
    return home, list_of_all_dirs


def get_dir_sizes(list_of_all_dirs):
    dir_sizes_dict = {}
    for directory in list_of_all_dirs:

        def _get_size_of_one_dir(dir):
            files = [i for i in dir.contents if i.size is not None]
            dirs = [i for i in dir.contents if i.size is None]
            return sum([c.size for c in files] + [_get_size_of_one_dir(d) for d in dirs])
        dir_sizes_dict[directory] = _get_size_of_one_dir(directory)
    return dir_sizes_dict


def part1(list_of_all_dirs: List[File]):
    dir_sizes_dict = get_dir_sizes(list_of_all_dirs)
    small_dirs = {k: v for k, v in dir_sizes_dict.items() if v <= 100000}
    return sum([v for k, v in small_dirs.items()])


def part2(home, list_of_all_dirs):
    dir_sizes_dict = get_dir_sizes(list_of_all_dirs)
    min_size_to_free_up = dir_sizes_dict[home] + 30000000 - 70000000
    size_to_delete = np.inf
    for _, size in dir_sizes_dict.items():
        if min_size_to_free_up < size < size_to_delete:
            size_to_delete = size
    return size_to_delete


def main():
    f = open("input.txt", "r")
    x = f.read().splitlines()
    home, list_of_all_dirs = parse_input(x)

    print(part1(list_of_all_dirs))
    print(part2(home, list_of_all_dirs))


if __name__ == '__main__':
    main()