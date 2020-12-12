usernames = input().split(", ")

valid_name = ""

for name in usernames:
    valid = True
    if 3 <= len(name) <= 16:
        for chr in name:
            if "@" in name:
                valid = False
                break
            if 65 <= ord(chr) <= 90 or 97 <= ord(chr) <= 122 or chr == "-" or chr == "_" or chr.isdigit():
                valid_name += chr
            else:
                valid = False
        if valid:
            print(valid_name)
        valid_name = ""
