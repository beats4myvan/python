targets = input().split()
tag = list(map(int, targets))

command = input()


def shooting(index, power):
    if len(tag) < index:
        return
    tag[index] = tag[index] - power
    if tag[index] <= 0:
        tag.remove(tag[index])
    return tag


def adding(index1, value1):
    if len(tag) < index:
        print(f"Invalid placement!")
        return tag
    else:
        tag.insert(index, value)
        return tag


def strike(index1, radius):
    if len(tag) > (index + (radius * 2)):
        target = 1 + (radius * 2)
        while target:
            tag.remove(tag[target])
            target -= 1
        return tag
    else:
        print(f'Strike missed!')
        return tag


while command != "End":
    command, index, value = command.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        shooting(index, value)
    elif command == "Add":
        adding(index, value)
    elif command == "Strike":
        strike(index, value)
    command = input()

    # command = input().split(" ")
    # command[1:] = list(map(int, command[1:]))

print("|".join([str(el) for el in tag]))
