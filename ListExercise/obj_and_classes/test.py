def alphabet_position(text):
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)

alp=input()
print(alphabet_position(alp))