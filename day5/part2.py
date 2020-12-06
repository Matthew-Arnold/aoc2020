import sys
import math
from collections import namedtuple

Seat = namedtuple('Seat', ['row', 'col'])

def do_thing(thing, low_key, high_key, start, stop):
    #print(thing)
    for char in thing:
        if char == low_key:
            start, stop = start, math.floor((stop + start) / 2)
        elif char == high_key:
            start, stop = math.floor((stop + start)) / 2, stop

        #print(start, stop)
    return stop

def seat_id(seat):
    return seat.row * 8 + seat.col

if __name__ == '__main__':
    ids = set()
    for line in sys.stdin:
        row = do_thing(line[:-3], 'F', 'B', 0, 127)
        col = do_thing(line[-4:], 'L', 'R', 0, 7)

        ids.add(seat_id(Seat(row, col)))
    
    for row in range(1, 127):
        for col in range(8):
            sample_id = seat_id(Seat(row, col))
            if sample_id not in ids and sample_id + 1 in ids and sample_id - 1 in ids:
                print(sample_id)
                #sys.exit(0)

    #print(seats)
        