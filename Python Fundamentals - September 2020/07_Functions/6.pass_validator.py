password1 = input()


def passwd_valid(password1):
    passwd = True
    if not 6 <= len(password1) <= 10:
        passwd = False
        print(f'Password must be between 6 and 10 characters')
    digits = 0
    for i in password1:

        if 48 <= ord(str(i)) <= 57:
            pass
        elif 65 <= ord(str(i)) <= 90:
            pass
        elif 97 <= ord(str(i)) <= 122:
            pass
        else:
            passwd = False
            print('Password must consist only of letters and digits')
            break
    for i in password1:

        if 48 <= ord(str(i)) <= 57:
            digits += 1
    if digits < 2:
        passwd = False
        print(f'Password must have at least 2 digits')
    if passwd:
        print(f'Password is valid')


passwd_valid(password1)
