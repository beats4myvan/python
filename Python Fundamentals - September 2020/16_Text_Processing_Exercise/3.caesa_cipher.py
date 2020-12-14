str = input().split("\\")

for i in str:
    if "." in i:
        name, extension = i.split(".")
        print(f'File name: {name}\nFile extension: {extension}')
