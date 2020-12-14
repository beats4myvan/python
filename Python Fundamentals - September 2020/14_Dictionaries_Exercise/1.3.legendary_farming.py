materials = input().split()
mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}

legend = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
while True:
    for i in range(0, len(materials), 2):
        item = materials[i + 1].lower()
        quantity = int(materials[i])
        if item in legend:
            legend[item] += quantity
            if legend[item] >= 250:
                legend[item] -= 250
                print(f'{mapper[item]} obtained!')
                obtained = True
                break
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity
    if obtained:
        break

    materials = input().split()

legend_ordered = sorted(legend.items(), key=lambda x: (-x[1], x[0]))

for key, value in legend_ordered:
    print(f'{key}: {value}')

junk = sorted(junk.items(), key=lambda x: x[0])
for key_junk, value_junk in junk:
    print(f'{key_junk}: {value_junk}')
