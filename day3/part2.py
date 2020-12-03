import sys
import math

def count_trees(grid, right, down):
    ndx = 0
    tree_count = 0

    for i in range(0, len(grid), down):
        row = grid[i]
        if row[ndx] == '#':
            tree_count += 1
        ndx = (ndx + right) % len(row)

    return tree_count

if __name__ == '__main__':
    grid = [line.strip() for line in sys.stdin]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(math.prod(count_trees(grid, slope[0], slope[1]) for slope in slopes))
