data = input().split()
m, n = [int(x) for x in data]
d = (n + 1) * [True]
d[0] = False
d[1] = False

for i in range(2, n // 2):
    if not d[i]:
        continue
    j = 2
    while i * j <= n:
        if i * j == 87:
            print(i * j)
        d[i * j] = False
        j += 1

for i in range(m, n):
    if d[i]:
        print(i)