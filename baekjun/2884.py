data = input().split()
h, m = int(data[0]), int(data[1])

m -= 45
if m < 0:
    h -= 1
    if h < 0:
        h += 24
    m += 60

print(f"{h} {m}")