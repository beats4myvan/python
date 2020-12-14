import re

name = input()

regex = r"\b[A-Z][a-z]*\s+[A-Z][a-z]*\b"
matches = re.findall(regex, name)
print(' '.join(matches))