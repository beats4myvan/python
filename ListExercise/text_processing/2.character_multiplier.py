str = input().split(" ")

str1 = str[0]
str2 = str[1]
total_sum = 0
if len(str1) < len(str2):
    for i in range(len(str1)):
        total_sum += ord(str1[i]) * ord(str2[i])
    if len(str1) > len(str2):
        left_str1 = str1[len(str1):]
        for i in left_str1:
          total_sum += ord(i)
    elif len(str1) < len(str2):
        left_str2 = str2[len(str1):]
        for i in left_str2:
            total_sum += ord(i)
else:
    for i in range(len(str2)):
        total_sum += ord(str1[i]) * ord(str2[i])
    if len(str1) > len(str2):
        left_str1 = str1[len(str2):]
        for i in left_str1:
            total_sum += ord(i)
    elif len(str1) < len(str2):
        left_str2 = str2[len(str1):]
        for i in left_str2:
            total_sum += ord(i)

print(total_sum)