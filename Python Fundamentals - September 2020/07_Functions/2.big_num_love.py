# def numbers(x):
#     nums = "".join(reversed(x))
#     final = ''
#     for num in nums:
#         if num is not " ":
#             final += "" + num
#     return final
# print(numbers(input()))

nums = input().split()
nums.sort(reverse=True)
for i in nums:
    print(i, end="")
