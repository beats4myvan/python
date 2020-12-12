houses = [int(n) for n in input().split("@")]

valentine_day_houses = len(houses)

command = input()
jump_pos = 0
while not command == "Love!":
    useless_str, jump = command.split()
    jump = int(jump)
    length_house = len(houses)
    jump_pos += jump
    if jump_pos >= length_house:
        jump_pos = 0
        jump = 0
    houses[jump_pos] = houses[jump_pos] - 2

    if houses[jump_pos] == 0:
        valentine_day_houses -= 1
        print(f"Place {jump_pos} has Valentine's day.")
    elif houses[jump] < 0:
        houses[jump_pos] = 0
        jump_pos = 0
        print(f"Place {houses[jump_pos]} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {jump_pos}.")

if valentine_day_houses == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {valentine_day_houses} places.")

