message = input()

command = input()

while command != 'Reveal':
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index_replace = int(command[1])
        message = f'{message[:index_replace]} {message[index_replace:]}'
        print(message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            revers_sub = substring[::-1]
            message += revers_sub
            print(message)
        else:
            print('error')
    elif command[0] == "ChangeAll":
        substring2 = command[1]
        replacement = command[2]
        message = message.replace(substring2, replacement)
        print(message)
    command = input()
print(f"You have a new text message: {message}")