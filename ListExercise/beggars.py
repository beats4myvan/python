numbers = input().split(', ')
beggars = int(input())
sums = [0] * beggars

while numbers:
    for index in range(beggars):
        if not numbers:
            break

        sums[index] += int(numbers.pop(0))

print(sums)






# numbers = input().split(' ')
# beggars = int(input())
#
# nums = list(numbers)
# sums = []
#
# for index in nums:
#     if beggars % int(index):
#          sums += nums
# print(sums)
