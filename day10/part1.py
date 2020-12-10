import sys

if __name__ == "__main__":
    data = sorted([int(line.strip()) for line in sys.stdin])

    count_three = 0
    count_one = 0

    prev = 0
    for d in data:
        if d - prev == 3:
            count_three += 1
        if d - prev == 1:
            count_one += 1
        
        prev = d

    count_three += 1
    print(count_one * count_three)