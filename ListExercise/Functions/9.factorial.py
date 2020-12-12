first = int(input())
second = int(input())
def factorial(first, second):

    factorial = 1
    
    for index in range(1, first+1):
        factorial *= index
    factorial /= second
    print(f'{factorial:.2f}')
factorial(first, second)