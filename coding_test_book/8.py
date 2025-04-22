import string

word = input()
nums = []
chars = []
for c in word:
    if c in string.ascii_uppercase:
        chars.append(c)
    else:
        nums.append(int(c))
head = ''.join(sorted(chars))
tail = str(sum(nums))
print(head + tail)
