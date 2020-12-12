gifts = input().split(' ')

command = input().split(' ')
while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]
        gifts = list(map(lambda lst: lst.replace(gift, "None"), gifts))

    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]

    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

    command = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')

for i in gifts:
    print(i, end=' ')

# test_list = [1, None, 4, None, None, 5, 8, None]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # using naive method
# # to remove None values in list
# res = []
# for val in test_list:
#     if val != None:
#         res.append(val)
#
#     # printing result
# print("List after removal of None values : " + str(res))
