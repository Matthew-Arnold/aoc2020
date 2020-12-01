import sys
import itertools

entries = [int(e.strip()) for e in sys.stdin]
target = 2020

vals = tuple((x, y) for x, y in itertools.combinations_with_replacement(entries, 2) if x + y == target)[0]

print(vals[0] * vals[1])