import sys
import itertools

entries = [int(e.strip()) for e in sys.stdin]
target = 2020

vals = tuple((x, y, z) for x, y, z in itertools.combinations_with_replacement(entries, 3) if x + y + z == target)[0]

print(vals[0] * vals[1] * vals[2])