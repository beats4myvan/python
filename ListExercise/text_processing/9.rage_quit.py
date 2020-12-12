line = input()

current_result = ''
result = ''

index = 0

while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ''
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1

        result += current_result.upper() * int(number)
        current_result = ''

print(f"Unique symbols used: {len(set(result))}")
print(result)