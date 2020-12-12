day_events = input().split('|')

energy = 100
max_energy = 100
initial_coins = 100
broke = False

for i in day_events:
    event, days = i.split('-')
    days = int(days)
    if event == 'rest':
        energy += days
        if energy > max_energy:
            energy -= days
            print(f'You gained 0 energy.')
        elif energy < max_energy:
            print(f'You gained {days} energy.')

        print(f'Current energy: {energy}.')
    elif event == 'order':
        initial_coins += days
        energy -= 30
        if energy < 0:
            energy += 80
            initial_coins -= days
            print(f'You had to rest!')
        else:
            print(f'You earned {days} coins.')
    else:
        initial_coins -= days
        if initial_coins <= 0:
            print(f'Closed! Cannot afford {event}. ')
            broke = True
            break

        print(f'You bought {event}.')
if not broke:
    print(f'Day completed! \nCoins: {initial_coins} \nEnergy: {energy}')




