n1 = input().split(', ')
n2 = input().split(', ')
file = list

for num in n2:
    n22 = num[-3:]
    if num[-1:-3] == n1[-1:-3]:
        file.append(num)
print(file)
