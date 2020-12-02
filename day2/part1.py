import sys

acc = 0

for line in sys.stdin:
    bounds, value, password = line.strip().split()
    value = value[0]
    min_count, max_count = [int(b) for b in bounds.split('-')]

    num_appearances = len([c for c in password if c == value])

    if num_appearances >= min_count and num_appearances <= max_count:
        acc += 1

print(acc)