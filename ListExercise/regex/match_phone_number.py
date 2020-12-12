import re

name = input()

regex = r"\+359([\s-])2\1\d{3}\1\d{4}\b"

matches = re.finditer(regex, name)
matches = [p.group() for p in matches]
print(', '.join(matches))
