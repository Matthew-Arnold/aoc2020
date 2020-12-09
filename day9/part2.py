import sys

if __name__ == "__main__":
    preamble_length = 25
    all_numbers = []

    for line in sys.stdin:
        all_numbers.append(int(line.strip()))

    relevant = all_numbers[:preamble_length]
    illegal = -1

    for val in all_numbers[preamble_length:]:
        for i in relevant:
            for j in relevant:
                if i != j and i + j == val:
                    relevant.pop(0)
                    relevant.append(val)
                    break
            else:
                continue
            break
        else:
            illegal = val
            break

    for ndx, number in enumerate(all_numbers):
        acc = number
        nums = [number]

        while acc < illegal:
            ndx += 1
            acc += all_numbers[ndx]
            nums.append(all_numbers[ndx])
        
        if acc == illegal:
            print(min(nums) + max(nums))
            sys.exit(0)
