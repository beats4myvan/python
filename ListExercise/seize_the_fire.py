level_of_fire = input().split('#')
amount_of_water = int(input())

HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

effort = 0
put_out_fire = []

for fire in level_of_fire:
    type_of_fire, value = fire.split(" = ")
    value = int(value)
    if type_of_fire == 'High' and value not in HIGH:
        continue
    elif type_of_fire == 'Medium' and value not in MEDIUM:
        continue
    elif type_of_fire == 'Low' and value not in LOW:
        continue

    if amount_of_water >= value:
        amount_of_water -= value
        effort += value * 0.25
        put_out_fire.append(value)


print(f'Cells:')
for fire_value in put_out_fire:
    print(f" - {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")

