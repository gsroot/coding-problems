n = int(input())
plans = input().split()

curr = [0, 0]
for plan in plans:
    if plan == 'U' and curr[0] > 0:
        curr[0] -= 1
    elif plan == 'D' and curr[0] < n - 1:
        curr[0] += 1
    elif plan == 'L' and curr[1] > 0:
        curr[1] -= 1
    elif plan == 'R' and curr[1] < n - 1:
        curr[1] += 1
print(curr[0] + 1, curr[1] + 1)