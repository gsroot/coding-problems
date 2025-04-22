n = int(input())
stack = list()

for i in range(n):
    data = input().split()
    if data[0] == 'push':
        stack.append(data[1])
    elif data[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif data[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
