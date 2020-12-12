strings = input().split(" ")

searched_palindrome = input()

palindromes = []

for word in strings:
    word1 = "".join(reversed(word))
    if word == word1:

        palindromes.append(word)

print(f"{palindromes}")

print(f"Found palindrome {palindromes.count(searched_palindrome)} times")