import sys

def count_bags(rules, start):
    if not rules.get(start):
        return 1
    return 1 + sum(thing[1] * count_bags(rules, thing[0]) for thing in rules[start])

if __name__ == "__main__":
    first = 'shinygold'
    rules = {}
    for line in sys.stdin:
        line = line.strip()
        source, dests = line.split('contain')
        source = ''.join(source.split()[:2])
        rules[source] = []

        for dest in dests.split(','):
            if dest.split()[0] != 'no':
                rules[source].append((''.join(dest.split()[1:3]), int(dest.split()[0])))

    print(count_bags(rules, first) - 1)
