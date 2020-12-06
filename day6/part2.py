import sys

if __name__ == '__main__':
    groups = []
    cur = []
    for line in sys.stdin:
        if len(line.strip()) == 0:
            groups.append(cur)
            cur = []
        else:
            cur.append(line.strip())

    groups.append(cur)

    count = 0 
    for group in groups:
        counts = {}
        for person in group:
            for thing in person:
                counts[thing] = counts.get(thing, 0) + 1

        #print(counts)
        count += sum(1 for count in counts if counts[count] == len(group))

    print(count)
