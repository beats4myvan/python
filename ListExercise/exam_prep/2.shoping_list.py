initial_list = input().split("!")

command = input()


def urgent(item):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item):
    if item in initial_list:
        initial_list.remove(item)


def correct(olditem, newitem):
    if olditem in initial_list:
        current_index = initial_list.index(olditem)
        initial_list[current_index] = newitem


def rearrange(item):
    if item in initial_list:                            
        initial_list.remove(item)
        initial_list.append(item)


while command != "Go Shopping!":    
    command = command.split()
    if command[0] == "Urgent":
        urgent(command[1])
    elif command[0] == "Unnecessary":
        unnecessary(command[1])
    elif command[0] == "Correct":
        correct(command[1], command[2])
    elif command[0] == "Rearrange":
        rearrange(command[1])
    command = input()
print(", ".join(initial_list))

