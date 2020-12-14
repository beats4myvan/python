line = input()
new_str = ""
old_letter = ""
for letter in line:
    if not letter == old_letter:
        new_str += letter
    old_letter = letter
print(new_str)