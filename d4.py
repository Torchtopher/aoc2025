with open("inputs/d4.txt", "r") as f:
    data = f.read().split()

x_len = len(data[0])
y_len = len(data)
total_p1 = 0
previous_total = -1

def has_four_paper_around(data: list[str], y, x):
    if data[y][x] == ".":
        return False

    up_valid    = True if y != 0 else False
    down_valid  = True if y != y_len - 1 else False
    left_valid  = True if x != 0 else False
    right_valid = True if x != x_len - 1 else False

    count = 0

    if right_valid and data[y][x+1] == "@": count += 1
    if left_valid  and data[y][x-1] == "@": count += 1
    if up_valid    and data[y-1][x] == "@": count += 1
    if down_valid  and data[y+1][x] == "@": count += 1

    if up_valid:
        if right_valid and data[y-1][x+1] == "@": count += 1
        if left_valid  and data[y-1][x-1] == "@": count += 1

    if down_valid:
        if right_valid and data[y+1][x+1] == "@": count += 1
        if left_valid  and data[y+1][x-1] == "@": count += 1

    # less than 4 around
    if count < 4:
        return True

# p1
for y, val in enumerate(data):
    for x, char in enumerate(val):
        if has_four_paper_around(data, y, x):
            total_p1 += 1

# p2
total_p2 = 0
previous_total = -1

while total_p2 != previous_total:
    previous_total = total_p2
    total_p2 = 0
    for y, val in enumerate(data):
        for x, char in enumerate(val):
            if has_four_paper_around(data, y, x):
                total_p2 += 1
                data[y] = data[y][:x] + "." + data[y][x+1:]

print(f"Total p1 {total_p1}")
print(f"Total p2 {total_p2}")

