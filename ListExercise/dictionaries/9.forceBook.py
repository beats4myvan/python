force_book_dict = {}
users = {}

command = input()
while not command == 'Lumpawaroo':

    if '|' in command:
        flag = False
        side, user = command.split(' | ')
        if user not in users:
            users[user] = side

    elif '-' in command:
        user, side = command.split(' -> ')
        users[user] = side
        print(f'{user} joins the {side} side!')

    command = input()

for key, value in users.items():
    if value not in force_book_dict:
        force_book_dict[value] = []
        force_book_dict[value].append(key)
    else:
        force_book_dict[value].append(key)

force_book_dict = dict(sorted(force_book_dict.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in force_book_dict.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for el in sorted(value):
            print(f'! {el}')
