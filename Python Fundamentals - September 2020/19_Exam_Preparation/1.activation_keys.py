activation_key = input()

command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        upOrLow = command[1]
        startIndex = int(command[2])
        endIndex = int(command[3])
        to_replace = activation_key[startIndex:endIndex]
        if upOrLow == "Upper":
            activation_key = activation_key.replace(to_replace, to_replace.upper())
        elif upOrLow == "Lower":
            activation_key = activation_key.replace(to_replace, to_replace.lower())
        print(activation_key)
    elif command[0] == 'Slice':
        startIndex = int(command[1])
        endIndex = int(command[2])
        activation_key = f'{activation_key[:startIndex]}{activation_key[endIndex:]}'
        print(activation_key)
    command = input()
print(f'Your activation key is: {activation_key}')
