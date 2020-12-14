# n = int(input())

def perf_num(n):
    sum = 0
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            sum += i
    return("We have a perfect number!" if sum == n else "it's not so perfect.")
print(perf_num(int(input())))