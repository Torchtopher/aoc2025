import math
from collections import Counter 
from copy import deepcopy
REAL = True

if REAL:
    file = "inputs/d8.txt"
else:
    file = "inputs/d8test.txt"
with open(file, "r") as f:
    data = f.read().split()

closest_lookup = {}

data = [list(map(int, x.split(","))) for x in data]

circuts_p1 = {}
circuts_p2 = {}

for idx1, p1 in enumerate(data):
    circuts_p1[(*p1,)] = 0
    circuts_p2[(*p1,)] = 0

    for idx2, p2 in enumerate(data): 
        dist = math.dist(p1, p2)
        closest_lookup[(*p1, *p2)] = dist

sorted_list_p1 = list(filter(lambda x: x[1] != 0, sorted(closest_lookup.items(), key=lambda item: item[1])))
sorted_list_p2 = deepcopy(sorted_list_p1)

def process(circuts: dict, sorted_list: list):
    global current_circut
    point = sorted_list.pop(0)
    point = sorted_list.pop(0)
    p1, p2 = point[0][:3], point[0][3:]
    p1_circut = circuts[p1]
    p2_circut = circuts[p2]
    if not p1_circut and not p2_circut:
        circuts[p1] = current_circut
        circuts[p2] = current_circut
        current_circut += 1
    elif p1_circut and p2_circut:
        # merge p1 and p2
        for key, val in circuts.items():
            if val == p2_circut:
                circuts[key] = p1_circut
    elif p1_circut:
        circuts[p2] = p1_circut
    elif p2_circut:
        circuts[p1] = p2_circut
    else:
        assert False
    return p1[0] * p2[0]

current_circut = 1

for i in range(1000):
    process(circuts_p1, sorted_list_p1)
    
c = Counter(circuts_p1.values())
del c[0] # 0ths we don't care about
total_p1 = 1
# doesn't actually find the right number lmao but the counter is correct
for _, (item) in zip(range(3), sorted(c.values(), reverse=True)):
    total_p1 *= item

print(f"Total p1 {total_p1}")
total_p2 = 1
current_circut = 1

while len(set(circuts_p2.values())) > 1 or not all(circuts_p2.values()):
    total_p2 = process(circuts_p2, sorted_list_p2)

print(f"Total p2 {total_p2}")