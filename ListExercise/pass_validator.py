passwords = input()


def valid_password(passwords):
    is_valid = True
    digits = 0
    if not 6 <= len(passwords) <= 10:
        is_valid = False
        print(f"Password must be between 6 and 10 characters")
    for i in passwords:
        if not 65 <= ord(str(i)) <= 90:
            pass
        if not 48 <= ord(str(i)) <= 57:
            pass
        if not 97 <= ord(str(i)) <= 122:
            print(f'Password must consist only of letters and digits')
            break
        if 48 <= ord(str(i)) <= 57:
            digits += 1
    if digits < 2:
        is_valid = False
        print(f'Password must have at least 2 digits')
    if is_valid:
        print('Password is valid')

valid_password(passwords)