str1 = input()

command = input().split()


def take_odd(string):
    newstr = ""
    for chr in string[1::2]:
        newstr += chr
    print(newstr)
    return newstr


def cut(str1, index, lenght):
    new_str = ''
    new_str1 = str1[:index]
    cut_str = str1[index+lenght:]
    new_str = new_str1 + cut_str
    print(new_str)
    return new_str

def substitute(str1, substring, substitute):
    if substring in str1:
        new_str = str1.replace(substring,substitute)
        print(new_str)
        return new_str
    else:
        print('Nothing to replace!')
        return str1

while not command[0] == "Done":
    if command[0] == "TakeOdd":
        str1 = take_odd(str1)
    elif command[0] == "Cut":
        str1 = cut(str1, int(command[1]), int(command[2]))
    elif command[0] == "Substitute":
        str1 = substitute(str1, command[1], command[2])
    command = input().split()

print(f"Your password is: {str1}")
