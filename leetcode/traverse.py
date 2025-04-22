def a(arr, a, b, direction, target):
    a += direction[target]
    cond = a >= len(arr) if target == 'row' else a >= len(arr[0])
    if a < 0 or cond or arr[a][b] is None:
        a += -direction[target]
        direction[target] = -direction[target]
        target = 'col' if target == 'row' else 'row'
        b += direction[target]
    return a, b, target

def traverse_arr(arr):
    i = 0
    j = 0
    target = 'row'
    direction = {'row': 1, 'col': 1}
    result = []
    while 0 <= i < len(arr) and 0 <= j < len(arr[0]) and arr[i][j] is not None:
        result.append(arr[i][j])
        arr[i][j] = None
        if target == 'row':
            i, j, target = a(arr, i, j, direction, target)
        else:
            j, i, target = a(arr, j, i, direction, target)
    return result


result = traverse_arr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)