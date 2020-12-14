import re

count_barcodes = int(input())

for i in range(count_barcodes):
    line = input()
    pattern = r"@#+[A-Z][a-zA-Z0-9]+[A-Z]\@\#+"
    # match = re.finditer(pattern,line)

    result = [el.group() for el in re.finditer(pattern, line)]
    if result:
        digit = ''
        count = 0
        for i in str(result):
            if i.isdigit():
                digit += i
            if i.isalpha() or i.isdigit():
                count += 1
        if len(digit) > 0 and count >= 6:
            print(f"Product group: {digit}")
        elif count >=6:
            print("Product group: 00")
        else:
            print("Invalid barcode")

    else:
        print("Invalid barcode")
