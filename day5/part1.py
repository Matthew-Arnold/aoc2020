import sys
import math

def do_thing(thing, low_key, high_key, start, stop):
    #print(thing)
    for char in thing:
        if char == low_key:
            start, stop = start, math.floor((stop + start) / 2)
        elif char == high_key:
            start, stop = math.floor((stop + start)) / 2, stop

        #print(start, stop)
    return stop

if __name__ == '__main__':
    scores = []
    for line in sys.stdin:
        row = do_thing(line[:-3], 'F', 'B', 0, 127)
        col = do_thing(line[-4:], 'L', 'R', 0, 7)

        scores.append(row * 8 + col)
    
    print(max(scores))
        