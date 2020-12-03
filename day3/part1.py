import sys

grid = [line.strip() for line in sys.stdin]

ndx = 0
tree_count = 0

for row in grid:
    if row[ndx] == '#':
        tree_count += 1
    ndx = (ndx + 3) % len(row)

print(tree_count)