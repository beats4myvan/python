import re
string = input()


destination = []
travel_points = ""
pattern = r'(?<=(\=|\/))[A-Z][A-Za-z]{2,}(?=\1)'

match = re.finditer(pattern, string)

for matched in match:
    travel_points += matched.group()
    destination.append(matched.group())

print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {len(travel_points)}")


