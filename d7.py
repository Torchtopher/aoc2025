from itertools import pairwise, zip_longest, chain 
import operator 
from collections import deque
from ordered_set import OrderedSet

with open("inputs/d7.txt", "r") as f:
    data = f.read().splitlines()

print(data)

done = False

# y, x
to_visit = {(0, data[0].index("S")): "exists"}
#print(to_visit)
times_hit_existing = 0
total_p1 = 0
#num_splitters = sum([x.count("^") for x in data])
# for i in range(10000):
    # y, x = next(iter(to_visit))
    # print(to_visit.keys())
    # if y == len(data) - 1:
    #     continue
    # print(y, x)
    # print(data[y+1])
    # new_pos = data[y+1][x]
    # print(new_pos)
    # if new_pos == ".":
    #     if (y+1, x) in to_visit:
    #         times_hit_existing += 1
    #     to_visit[(y+1, x)] = "exists"
    #     del to_visit[(y, x)]
    #     continue
    # elif new_pos == "^":
    #     print("adding 1")
    #     total_p1 += 1
    #     if (y+1, x-1) in to_visit:
    #         times_hit_existing += 1
    #     if (y+1, x+1) in to_visit:
    #         times_hit_existing += 1
    #     to_visit[(y+1, x+1)] = "exists"
    #     to_visit[(y+1, x-1)] = "exists"
    #     del to_visit[(y, x)]

    # else: assert False
'''
[(141, 140), (141, 138), (141, 137), (141, 136), (141, 134), (141, 132), (141, 131), (141, 130), (141, 128), (141, 126), (141, 124), (141, 122), (141, 120), (141, 119), (141, 118), (141, 116), (141, 114), (141, 113), (141, 112), (141, 110), (141, 108), (141, 106), (141, 104), (141, 103), (141, 101), (141, 100), (141, 98), (141, 96), (141, 94), (141, 92), (141, 91), (141, 90), (141, 88), (141, 86), (141, 84), (141, 82), (141, 80), (141, 79), (141, 78), (141, 76), (141, 74), (141, 73), (141, 72), (141, 70), (141, 68), (141, 67), (141, 66), (141, 64), (141, 63), (141, 62), (141, 60), (141, 58), (141, 57), (141, 56), (141, 54), (141, 52), (141, 50), (141, 48), (141, 46), (141, 45), (141, 44), (141, 42), (141, 40), (141, 38), (141, 37), (141, 35), (141, 34), (141, 32), (141, 31), (141, 30), (141, 28), (141, 27), (141, 26), (141, 24), (141, 22), (141, 21), (141, 20), (141, 18), (141, 17), (141, 16), (141, 14), (141, 13), (141, 12), (141, 10), (141, 8), (141, 6), (141, 4), (141, 2), (141, 0)]
[(15, 14), (15, 12), (15, 11), (15, 10), (15, 8), (15, 6), (15, 4), (15, 2), (15, 0)]
'''
total_p2 = 0
solved = {}

# goes checks both sides of a splitter
def check_splitter(data, y, x):
    total_beams = 0
    t_y = y
    # left and right, yes its bad
    while True:
        if t_y+1 == len(data) - 1: # hit end so only one
            total_beams += 1
            break
        elif data[t_y+1][x+1] == "^":
            total_beams += solved[(t_y+1, x+1)]
            break
        t_y += 1

    t_y = y
    while True:
        if t_y+1 == len(data) - 1: 
            total_beams += 1
            break
        elif data[t_y+1][x-1] == "^":
            total_beams += solved[(t_y+1, x-1)]
            break
        t_y += 1
    
    return total_beams


for y_idx, row in reversed(list(enumerate(data))):
    print(y_idx, row)
    if "^" not in row:
        continue
    for x_idx, val in enumerate(row):
        if val == "^":
            solved[(y_idx, x_idx)] = check_splitter(data, y_idx, x_idx)

print(solved)