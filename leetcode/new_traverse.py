

def traverse(arr):
    y = 0
    x = 0
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    i = 0
    m = moves[0]
    result = []
    while not (y >= len(arr) or y < 0 or x >= len(arr[0]) or x < 0 or arr[y][x] == 0):
        result.append(arr[y][x])
        arr[y][x] = 0
        y += m[0]
        x += m[1]
        if y >= len(arr) or y < 0 or x >= len(arr[0]) or x < 0 or arr[y][x] == 0:
            y -= m[0]
            x -= m[1]
            i += 1
            m = moves[i % 4]
            y += m[0]
            x += m[1]
    return result



result = traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)