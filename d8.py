import math
from collections import Counter 

with open("inputs/d8test.txt", "r") as f:
    data = f.read().split()

print(data)
closest_lookup = {}

data = [list(map(int, x.split(","))) for x in data]
print(data)

circuts = {}



for idx1, p1 in enumerate(data):
    circuts[(*p1,)] = 0
    for idx2, p2 in enumerate(data): 
        dist = math.dist(p1, p2)
        closest_lookup[(*p1, *p2)] = dist

#print(closest_lookup)
print(len(closest_lookup))
sorted_list = list(filter(lambda x: x[1] != 0, sorted(closest_lookup.items(), key=lambda item: item[1])))
#print(circuts)

current_circut = 1
for i in range(10):
    point = sorted_list.pop(0)
    point = sorted_list.pop(0) # hacky dedup
    p1, p2 = point[0][:3], point[0][3:]
    p1_circut = circuts[p1]
    p2_circut = circuts[p2]
    if not p1_circut and not p2_circut:
        circuts[p1] = current_circut
        circuts[p2] = current_circut
        current_circut += 1
    elif p1_circut:
        circuts[p2] = p1_circut
    elif p2_circut:
        circuts[p1] = p2_circut
    else:
        assert False

    print(p1, p2)
    print(circuts)
    input()

c = Counter(circuts.values())
print(c)