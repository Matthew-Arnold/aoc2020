import sys

acc = 0

for line in sys.stdin:
    bounds, value, password = line.strip().split()
    value = value[0]
    first, second = [int(b) - 1 for b in bounds.split('-')]

    if (password[first] == value) ^ (password[second] == value):
        acc += 1

print(acc)