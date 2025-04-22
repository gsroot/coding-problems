from collections import deque

data = input().split()
n, m, v = int(data[0]), int(data[1]), int(data[2])
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    data = [int(x) for x in input().split()]
    x, y = data[0], data[1]
    graph[x - 1][y - 1] = 1


def dfs(val, visit):
    visit[val - 1] = True
    result = [val]
    for i in range(len(graph[val - 1])):
        if visit[i] or graph[val - 1][i] == 0:
            continue
        result += dfs(i + 1, visit)
    return result


def bfs(val):
    q = deque([val])
    visit = n * [False]
    visit[val - 1] = True
    result = []
    while q:
        val = q.popleft()
        result.append(val)
        for i in range(len(graph[val - 1])):
            if visit[i] or graph[val - 1][i] == 0:
                continue
            q.append(i + 1)
            visit[i] = True
    return result


result = dfs(v, n * [False])
print(' '.join([str(x) for x in result]))
result = bfs(v)
print(' '.join([str(x) for x in result]))
