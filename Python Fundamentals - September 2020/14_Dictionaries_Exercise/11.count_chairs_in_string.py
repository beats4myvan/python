character = input()
dictionary = {}

for i in character:
    if i == ' ':
        continue
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1
for el in dictionary:
    print(f'{el} -> {dictionary[el]}')