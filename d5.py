
with open("inputs/d5.txt", "r") as f:
    ranges, ingredients = f.read().split("\n\n")

ranges = ranges.split()
ingredients = list(map(int, ingredients.split()))

ranges = [range(int(x.split("-")[0]), int(x.split("-")[1]) + 1) for x in ranges]

total_p1 = 0
for i in ingredients:
    for r in ranges:
        if i in r:
            total_p1 += 1
            break

print(f"total p1 {total_p1}")

ranges.sort(key=lambda x: x.start)
total_p2 = 0
largest_end = 0
for r in ranges:
    total_p2 += max(0, r.stop - max(r.start, largest_end))
    largest_end = max(r.stop, largest_end)

print(f"total p2 {total_p2}")
