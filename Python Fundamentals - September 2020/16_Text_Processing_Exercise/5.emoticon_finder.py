text = input().split()
chars = [char[i:i+2] for char in text for i in range(len(char)) if char[i] == ":"]
print('\n'.join(chars))


# string_list = input().split()
#
# emoticon_list = [el[i:i+2]
#                  for el in string_list
#                  for i in range(len(el))
#                  if el[i] == ":"]
# for emoticon in emoticon_list:
#     print(emoticon)