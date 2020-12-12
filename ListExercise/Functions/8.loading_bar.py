number = int(input())


def load_bar(n):
    load_bar = ''

    for num in range(number // 10):
        if num < number // 10:
            load_bar += "%"
    load_bar1 = 10 - (number // 10)
    load_bar += load_bar1 * "."

    if load_bar == '%%%%%%%%%%':
        return (f'{number}% Complete!\n[{load_bar}]')
    else:
        return (f'{number}% [{load_bar}]\nStill loading...')


print(load_bar(number))
