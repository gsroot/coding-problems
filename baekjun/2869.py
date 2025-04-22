a, b, v = [int(x) for x in input().split()]

line = v - a
result = line // (a - b)
remain = (line % (a - b))
if remain == 0:
    result += 1
else:
    result += 2

print(result)