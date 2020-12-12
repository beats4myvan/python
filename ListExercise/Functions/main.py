a1 = int(input())
b1 = int(input())
operator1 = input()
def solve(a,b,operator):
    result = None

    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    return result

print(solve(b1,a1,operator1))