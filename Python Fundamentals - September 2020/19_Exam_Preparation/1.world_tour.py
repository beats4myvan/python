vacation = input()

data = input()

while not data == 'Travel':
    command = data.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if len(vacation) > index:
            vacation = vacation[:index] + string + vacation[index:]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        stop_index = int(command[2])
        if len(vacation) > stop_index:
            vacation = vacation[:start_index] + vacation[stop_index+1:]
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        vacation = vacation.replace(old_string,new_string)
    print(vacation)
    data = input()
print(f"Ready for world tour! Planned stops: {vacation}")