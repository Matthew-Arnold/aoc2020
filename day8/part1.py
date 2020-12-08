import sys

if __name__ == "__main__":
    instructions = [(i[0], int(i[1])) for i in (line.strip().split() for line in sys.stdin)]
    visited = set()
    acc = 0

    i = 0
    while i < len(instructions):
        if i in visited:
            print(acc)
            break

        visited.add(i)
        instruction = instructions[i]

        operator, argument = instruction
        if operator == 'nop':
            i += 1
        elif operator == 'acc':
            acc += argument
            i += 1
        elif operator == 'jmp':
            i += argument

