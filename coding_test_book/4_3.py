import itertools

input_data = input()
x, y = ord(input_data[0]) - ord("a") + 1, int(input_data[1])

moves = list(itertools.permutations([-2, -1, 1, 2], 2))
moves = [x for x in moves if abs(x[0]) != abs(x[1])]

count = 0
for (mx, my) in moves:
    nx = x + mx
    ny = y + my
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1
print(count)