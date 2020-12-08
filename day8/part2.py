import sys

class Cycle(Exception):
    pass

def do_thing(instructions):
    visited = set()
    acc = 0
    i = 0
    while i < len(instructions):
        if i in visited:                
            raise Cycle()

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

    return acc


if __name__ == "__main__":
    instructions = [(i[0], int(i[1])) for i in (line.strip().split() for line in sys.stdin)]

    for ndx, instruction in enumerate(instructions):
        if instruction[0] == 'jmp':
            new_instruction = ('nop', instruction[1])
            instructions[ndx] = new_instruction
        elif instruction[0] == 'nop':
            new_instruction = ('jmp', instruction[1])
            instructions[ndx] = new_instruction
        
        try:                
            print(do_thing(instructions))
            exit(0)
        except Cycle:               
            instructions[ndx] = instruction
