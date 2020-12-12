import re

string = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+[a-z.-]+\.[a-z]+"

match = re.finditer(pattern, string)

for matched in match:

    print(matched.group())
