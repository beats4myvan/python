substrings = input().split(', ')
second_list = input()
#
# # unique = (list(filter(lambda x: x in second_list, substrings)))
# # print(unique)
unique = [i for i in substrings
          if i in second_list]
print(unique)
