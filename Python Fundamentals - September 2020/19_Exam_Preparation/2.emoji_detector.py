import re

text = input()

pattern = r"(:{2}|\*{2})(?P<emoji>[A-Z]{1}[a-z]{2,})\1"

cool_threshold = 1
numbers = re.findall(r"\d", text)

for n in range(len(numbers)):
    cool_threshold *= int(numbers[n])

emojis_dict = {}
emojis = re.finditer(pattern, text)
for emoji in emojis:
    emoji_value = 0
    e = emoji.group()
    for char in e:
        if char != ':' and char != "*":
            emoji_value += ord(char)
    emojis_dict[e] = emoji_value

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_dict)} emojis found in the text. The cool ones are:")
for el in emojis_dict:
    if emojis_dict[el] >= cool_threshold:
        print(el)