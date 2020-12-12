

word = input()
dig = ''
chars = ''
elses = ''
for i in word:
    if i.isdigit():
        dig += i
    elif i.isalpha():
        chars += i
    else:
        elses += i
print(f"{dig}\n{chars}\n{ elses}")
