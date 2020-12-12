elements = input()
products = {}

while not elements == "statistics":
    elements = elements.split(": ")
    key = elements[0]
    value = elements[1]
    if not key in products:
        products[key] = int(value)
    else:
        products[key] += int(value)
    elements = input()
print(f'Products in stock:')
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f'Total Quantity: {sum(products.values())}')
