items = input().split('|')
budget = int(input())

ticket = 150
sell_profit = []
left_profit = 0

for i in items:
    type_, price = i.split("->")
    price = float(price)
    profit = 0
    if type_ == 'Clothes' and price <= 50 and price < budget:
        budget -= price
        profit += price * 0.40
        left_profit += price * 0.40
        sell_profit.append(profit + price)
    elif type_ == 'Shoes' and price <= 35 and price < budget:
        budget -= price
        profit += price * 0.40
        left_profit += price * 0.40
        sell_profit.append(profit + price)
    elif type_ == 'Accessories' and price <= 20.50 and price < budget:
        budget -= price
        profit += price * 0.40
        left_profit += price * 0.40
        sell_profit.append(profit + price)

# round_profit = [round(num, 2) for num in sell_profit]
for j in sell_profit:
    print(f'{j:.2f}', end=' ')

print()
print(f"Profit: {round(left_profit, 2)}")
if budget + (sum(sell_profit)) > ticket:
    print(f'Hello, France!')
else:
    print(f"Time to go.")
