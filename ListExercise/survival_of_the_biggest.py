# list = input().split(' ')
# list1 = list
# num = int(input())
# for i in range(num):
#     min1 = int(min(list1))
#     list1.remove(min(list1))
# print(list1)



numbers_str = input().split()

numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(numbers)