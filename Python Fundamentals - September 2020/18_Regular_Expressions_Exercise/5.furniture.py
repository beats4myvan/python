import re

line = input()
pattern = r"(>>)(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
names = []
total_price = 0

while line != 'Purchase':
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj["furniture"])
        total_price += float(obj["price"]) * int(obj["quantity"])

    line = input()
print(f"Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {total_price:.2f}")
