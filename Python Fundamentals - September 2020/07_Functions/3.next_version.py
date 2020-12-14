version = input().replace(".", "")
new_ver = int(version) + 1
new_ver_str = str(new_ver).replace("", ".")[1:6]
print(new_ver_str)