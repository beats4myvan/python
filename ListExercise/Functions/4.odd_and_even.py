def odd_even(a):
    
    odd = 0
    even = 0
    for i in num:
        i = int(i)
        if i % 2 == 1:
            odd += i
        else:
            even += i
    return odd, even

num = input().split(' ')

num = list(map(int, str(num[0])))

print(f'Odd sum = {(odd_even(num)[0])}, Even sum = {(odd_even(num)[1])}')
