gifts = input().split()
money = 'No Money'
gift = []

for i in range(len(gifts)):
    command = input()
    for j in command:
        if j == 'O':
            command, gift = command.split()
            gifts.insert(gift)
            break
        if j == 'R':
            command, gift, index = command.split()
            index = int(index)
            gifts.remove(gifts[index])
            gifts.append(gift)

print(gifts)
