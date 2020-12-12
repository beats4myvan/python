num = int(input())
nums = []
for index in range(num):
    num_of_electrons = 2*((index+1)**2)
    num -= num_of_electrons
    if not num <= 0:
        nums.append(num_of_electrons)

    if num <= 0:
        num += num_of_electrons
        nums.append(num)
        break
print(nums)
