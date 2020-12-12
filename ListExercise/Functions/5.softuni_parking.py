n = int(input())

parking_lot = {}

for _ in range(n):
    commands = input().split()

    if commands[0] == "register":
        command, username, license_plate = commands
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif commands[0] == "unregister":
        user = commands[1]
        if not user in parking_lot:
            print(f'ERROR: user {user} not found')
        else:
            del parking_lot[user]
            print(f'{user} unregistered successfully')
for i in parking_lot:
    print(f'{i} => {parking_lot[i]}')
