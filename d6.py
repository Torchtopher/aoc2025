from itertools import pairwise, zip_longest, chain 
import operator 
with open("inputs/d6.txt", "r") as f:
    data = f.read().splitlines()


ops = data.pop()
ops = ops.split()

numbers = []
for line in data:
    numbers.append(line.split())

#print(f"n {numbers}")

total_p1 = 0
for to_add, op in zip(zip(*numbers), ops): # just want op in its own var
    
    if op == "*":
        ans = 1
        for num in to_add:
            ans *= int(num)
        total_p1 += ans
    elif op == "+":
        ans = 0
        for num in to_add:
            ans += int(num)
        total_p1 += ans
    else: assert False

print(f"total p1 {total_p1}")

total_p2 = 0

with open("inputs/d6.txt", "r") as f:
    data = f.read().splitlines()


nums = [""] * (len(data) - 1) # number of lines w numbers 
current_op = operator.mul
first_time = True

for elements in chain(zip(*data), ["X"]): # X is just to signal we hit the end and need to add the last num
    if elements[-1] != " ": # we have an op, time to reset
        if first_time:
            current_op = operator.mul if elements[-1] == "*" else operator.add
            first_time = False
        else:
            ans = 1 if current_op == operator.mul else 0
            celphlepod_nums = []
            for n in zip_longest(*nums):
                try: celphlepod_nums.append(int(''.join(n)))
                except: pass

            for i in celphlepod_nums:
                ans = current_op(ans, i)
            total_p2 += ans
            nums = [""] * (len(data) - 1)
            current_op = operator.mul if elements[-1] == "*" else operator.add
    for idx, val in enumerate(elements):
        if idx == len(elements) - 1: break # don't want to add the op to nums
        nums[idx] += val

print(f"Total p2 {total_p2}")
