

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

password_p2 = 0

def calc(pos, i):
    starting_pos = pos
    move_amount = int(i[1:])

    to_add = 0

    mov_quot, move_amount = divmod(move_amount, 100)
    to_add += mov_quot

    if i[0] == "L":
        shifted = pos - move_amount
        quot, remainder = divmod(pos - move_amount, 100)
        pos = remainder
        
    if i[0] == "R":
        shifted = pos + move_amount
        quot, remainder = divmod(pos + move_amount, 100)
        pos = remainder

    
    # started at 0, and went left, need to account for negative mod
    to_add += abs(quot)
    if starting_pos == 0 and i[0] == "L":
        to_add -= 1
    if shifted == 0:
        to_add += 1
    
    return to_add, pos
    print(f"Adding {to_add} to pass")

def not_working(pos, i):
    starting_pos = pos
    move_amount = int(i[1:])

    print(move_amount)
    to_add =0 
    original_move_amount = move_amount


    if i[0] == "L":
        shifted = pos - move_amount
        quot, remainder = divmod(pos - move_amount, 100)
        print(f"Original quot remainder {divmod(pos - original_move_amount, 100)}")
        pos = remainder
        
    if i[0] == "R":
        shifted = pos + move_amount
        quot, remainder = divmod(pos + move_amount, 100)
        pos = remainder

    print(f"Quot {quot}, remainder {remainder}, pos {pos} move_amount {move_amount}, direction {i[0]}")
    
    # started at 0, and went left, need to account for negative mod
    to_add += abs(quot)
    if starting_pos == 0 and i[0] == "L":
        to_add -= 1
    if remainder == 0 and i[0] == "L":
        to_add += 1
    
    return to_add, pos
    print(f"Adding {to_add} to pass")

pos = 50
for i in data:
    to_add, pos = working(pos, i)
    assert working(pos, i) == not_working(pos, i), f"Failed on {i} at pos {pos} with {working(pos, i)} vs {not_working(pos, i)}"
    password_p2 += to_add
    



print(f"Password p2 is {password_p2}")