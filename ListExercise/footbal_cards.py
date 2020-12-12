red_card = input().split(' ')


A = range(1, 12)
B = range(1, 12)


game_was_terminated = False
for index in red_card:
    card, player = index.split('-')
    player = int(player)
    if card == 'A':
        if player not in A:
            continue
        A.remove(player)
    elif card == 'B':
        if player not in B:
            continue
        B.remove(player)
    if len(A) < 7 or len(B) < 7:
        game_was_terminated = True

        break
if game_was_terminated:
    print(f'Team A - {len(A)}; Team B - {len(B)}')
    print(f"Game was terminated")
else:
    print(f'Team A - {len(A)}; Team B - {len(B)}')