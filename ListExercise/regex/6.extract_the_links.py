import re

line = input()
sites = []
pattern = r"www.[0-9a-zA-Z-]+\.[a-z.]+"
while line:
    matchs = re.findall(pattern, line)
    if matchs:
        sites.extend(matchs)
    line = input()
print('\n'.join(sites))

