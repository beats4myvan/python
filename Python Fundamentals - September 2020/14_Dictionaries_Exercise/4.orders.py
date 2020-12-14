products = input()

database = {}

while not products == "buy":

    product, price, quantity = products.split(" ")
    if product not in database:
        database[product] = [float(price), int(quantity)]
    else:
        database[product][0] = float(price)
        database[product][1] += int(quantity)

    products = input()

for item in database:
    price = database[item][0] * database[item][1]
    print(f'{item} -> {price:.2f}')
