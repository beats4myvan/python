numbers = list(map(lambda x: int(x), input().split(",")))

GROUP_10 = range(1, 10)
GROUP_20 = range(10, 20)
GROUP_30 = range(20, 30)
GROUP_40 = range(30, 40)
GROUP_50 = range(40, 51)

GROUP10 = list()
GROUP20 = []
GROUP30 = []
GROUP40 = []
GROUP50 = list()

for num in numbers:
    if int(num) in GROUP_10:
        GROUP10.append(num)

    elif int(num) in GROUP_20:
        GROUP20.append(num)

    elif int(num) in GROUP_30:
        GROUP30.append(num)

    elif int(num) in GROUP_40:
        GROUP40.append(num)

    elif int(num) in GROUP_50:
        GROUP50.append(num)

print(f"Group of 10's: {GROUP10}")
print(f"Group of 20's: {GROUP20}")
print(f"Group of 30's: {GROUP30}")
print(f"Group of 40's: {GROUP40}")
if GROUP50:
    print(f"Group of 50's: {GROUP50}")
