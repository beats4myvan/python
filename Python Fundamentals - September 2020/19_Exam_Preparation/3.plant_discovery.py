n = int(input())

discovered_plants = {}
ratings = 0
for _ in range(n):
    discovered = input().split("<->")
    plant, rarity = discovered
    if plant in discovered_plants:
        discovered_plants[plant] += {'rare': int(rarity), 'rating': []}
    else:
        discovered_plants[plant] = {'rare': int(rarity), 'rating': []}

command = input()
while not command == "Exhibition":
    command, value = command.split(': ')

    if command == "Rate":
        plant, rating = value.split(" - ")
        if plant not in discovered_plants:
            print('error')
        else:
            discovered_plants[plant]['rating'].append(int(rating))

    elif command == 'Update':
        plant, rarity = value.split(" - ")
        if plant not in discovered_plants:
            print('error')
        else:
            discovered_plants[plant]['rare'] = int(rarity)

    elif command == 'Reset':
        plant = value
        if plant not in discovered_plants:
            print('error')
        else:
            discovered_plants[plant]['rating'].clear()

    command = input()

for plant_name, plants_data in discovered_plants.items():
    if discovered_plants[plant_name]['rating']:
        discovered_plants[plant_name]['avg'] = sum(discovered_plants[plant_name]['rating']) / len(
            discovered_plants[plant_name]['rating'])
    else:
        discovered_plants[plant_name]['avg'] = 0

sorted_plants = sorted(discovered_plants.items(), key=lambda x: (x[1]['rare'], x[1]['avg']), reverse=True)

print('Plants for the exhibition:')
for i, x in sorted_plants:
    print(f"- {i}; Rarity: {x['rare']}; Rating: {x['avg']:.2f}")
