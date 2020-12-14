number_of_rooms = int(input())

chairs_left = 0
game_on = True
for room1 in range(1, number_of_rooms + 1):

    room = input().split(" ")
    chairs = len(room[0])
    taken_seeds = int(room[1])

    if chairs > taken_seeds:
        chairs_left += chairs - taken_seeds
    elif chairs < taken_seeds:
        game_on = False
        print(f'{(taken_seeds - chairs)} more chairs needed in room {room1} ')

if game_on:
    print(f'Game On, {chairs_left} free chairs left')