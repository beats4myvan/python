line = input().split(" ")

def alphabet_position(text):
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)

numbers = []
fin_num = []
num = ""
for i in line:
    if i == "":
        continue

    numbers = []
    num=""
    for n in i:
        if n.isdigit():
            num += n
    if i[0].isupper():
        numbers = int(num) / int(alphabet_position(i[0]))
    elif i[0].islower():
        numbers = int(num) * int(alphabet_position(i[0]))
    next_letter = i[int(len(num))+1::]
    if next_letter.isupper():
        numbers = float(numbers) - int(alphabet_position(next_letter))
        fin_num.append(numbers)
    elif next_letter.islower():
        numbers = float(numbers) + int(alphabet_position(next_letter))
        fin_num.append(numbers)

print(f"{sum(fin_num):.2f}")

