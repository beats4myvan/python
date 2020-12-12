import re

pattern = r"\b(\d{2})(?P<separator>[-/.])([A-Z][a-z]{2})(?P=separator)(?P<year>\d{4}\b)"

text = input()

matches = re.findall(pattern, text)
for matches in matches:
    print(f"Day: {matches[0]}, Month: {matches[2]}, Year: {matches[3]}")
