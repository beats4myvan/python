import re

pattern = r"(?<=\s_)([a-zA-Z0-9]+)($|(?=\s))"

line = input()

result = [el.group() for el in re.finditer(pattern, line)]
print(','.join(result))