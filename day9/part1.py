import sys

if __name__ == "__main__":
    preamble_length = 25
    numbers = []

    for _ in range(preamble_length):
        numbers.append(int(sys.stdin.readline().strip()))

    for line in sys.stdin:
        val = int(line.strip())
        for i in numbers:
            for j in numbers:
                if i != j and i + j == val:
                    numbers.pop(0)
                    numbers.append(val)
                    break
            else:
                continue
            break
        else:
            print(val)
            sys.exit(0)