
with open("inputs/d3.txt", "r") as f:
    data = f.read().split()

print(data)

n_numbers = 12
total_p1 = 0

for battery in data:
    number = [0] * n_numbers
    for b_idx, char in enumerate(battery):
        joltage_val = int(char)
        for idx, num in enumerate(number):
            spaces_remaning = len(battery) - (b_idx + 1) # how many spaces we have left on the battery
            number_spaces_remaning = len(number[idx+1:]) # how many space we need to fill in number
            if number_spaces_remaning > spaces_remaning:
                continue 
            if joltage_val > num:
                number[idx] = joltage_val
                for i, item in enumerate(number[idx+1:]):
                    number[i + idx + 1] = 0 # remaning numbers are invalid because we updated a value in front 
                break

    total_p1 += int(''.join(map(str,number)))
    print(f"Adding {int(''.join(map(str,number)))}")
print(f"Total p1 {total_p1}")