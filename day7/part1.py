import sys

def can_hold(rules, current, target):
    if target in rules.get(current, []):
        return True
    for next in rules.get(current, []):
        if can_hold(rules, next, target):
            return True
    return False

if __name__ == "__main__":
    goal = 'shinygold'
    rules = {}
    for line in sys.stdin:
        line = line.strip()
        source, dests = line.split('contain')
        source = ''.join(source.split()[:2])
        rules[source] = []

        for dest in dests.split(','):
            rules[source].append(''.join(dest.split()[1:3]))

    print(sum(1 for rule in rules if can_hold(rules, rule, goal)))