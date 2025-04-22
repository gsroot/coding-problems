input_data = input().split()
h, m = int(input_data[0]), int(input_data[1])
c = int(input())

h = (h + ((m + c) // 60)) % 24
m = (m + c) % 60
print(f"{h} {m}")