

with open("inputs/d1.txt", "r") as f:
    data = f.read().split()

print(data)

pos = 50
password = 0
for i in data:
    move_amount = int(i[1:])
    print(move_amount)

    if i[0] == "L":
        pos -= move_amount
        pos = pos % 100

    if i[0] == "R":
        pos += move_amount
        pos = pos % 100

    if pos == 0:
        password += 1 

print(f"Password is {password}")

pos = 50
password_p2 = 0

for i in data:
    move_amount = int(i[1:])

    if i[0] == "L":
        for _ in range(move_amount):
            pos -= 1
            if pos == -1:
                pos = 99
            if pos == 0:
                password_p2 += 1
        
    if i[0] == "R":
        for _ in range(move_amount):
            pos += 1
            if pos == 100:
                pos = 0
            if pos == 0:
                password_p2 += 1

print(f"password p2 {password_p2}")