
def palindrome_int(a):

    for num in pos_integers:
        num1 = int(num[::-1])
        num = int(num)

        if num == num1:
            return "True"
        else:
            return "False"
pos_integers = input().split(",")

print(palindrome_int(pos_integers))