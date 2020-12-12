import re
line = input()
pattern = r'(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

match = re.findall(pattern, line)
mirrors = []
mirror_word = False
for i in match:
    first_w = i[1]
    second_w = i[2]
    if first_w == second_w[::-1]:
        mirrors.append(first_w + " " "<=>" " "+ second_w)
        mirror_word = True

if len(match) > 0:
    print(f"{len(match)} word pairs found!")
else:
    print(f"No word pairs found!")
if mirror_word:
    print("The mirror words are:")
    print(f', '.join(mirrors))
else:
    print("No mirror words!")
