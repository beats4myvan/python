import re

data = input()

searched = input()

pattern = f"\\b{searched}\\b"

find = re.findall(pattern, data, re.IGNORECASE)
print(len(find))