input_data = input().split()
n, m = int(input_data[0]), int(input_data[1])
arr = []
for i in range(n):
    arr.append(list(map(int, input())))


def dfs(x, y):
    if not 0 <= x < m or not 0 <= y < n:
        return
    if arr[y][x] == 0:
        arr[y][x] = 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    else:
        return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(j, i):
            result += 1
print(result)