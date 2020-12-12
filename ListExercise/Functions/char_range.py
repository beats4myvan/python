first = input()
second = input()


def characters(first, second):
    first = ord(first)
    second = ord(second)
    sum = ''
    for j in range(first + 1, second):
        sum += chr(j) + " "
    for j in range(second + 1, first):
        sum += chr(j) + " "
    return sum


print(characters(first, second))
