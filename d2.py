with open("inputs/d2.txt", "r") as f:
    data = f.read().split(",")

def is_id_invalid_p1(num_str):
    if len(num_str) % 2 != 0:
        return False
    middle_idx = int(len(num_str) / 2)
    if num_str[:middle_idx] == num_str[middle_idx:]:
        return True


def is_id_invalid_p2(num_str):
    middle_idx = int(len(num_str) / 2)
    if num_str[:middle_idx] == num_str[middle_idx:]:
        return True
    # try 1 len combos, 2 len, etc
    for i in range(1, middle_idx+1):
        base = num_str[:i]
        multipler = (len(num_str) // len(base))

        if num_str == base * multipler:
            return True
    return False


total_p1 = 0
for id_range in data:
    start, end = id_range.split("-")
    start, end = int(start), int(end)
    
    for i in range(start, end+1):
        if is_id_invalid_p1(str(i)):
            total_p1 += i

print(f"Final p1 {total_p1}")

total_p2 = 0
for id_range in data:
    start, end = id_range.split("-")
    start, end = int(start), int(end)
    
    for i in range(start, end+1):
        if is_id_invalid_p2(str(i)):
            total_p2 += i
            print(f"Invalid ID {i}")

print(f"Final p2 {total_p2}")
