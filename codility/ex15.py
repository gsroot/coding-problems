def solution(A):
    cnt = 0
    min_x_list = []
    max_x_list = []
    for i in xrange(len(A)):
        min_x_list.append(i - A[i])
        max_x_list.append(i + A[i])
    min_x_list.sort()
    max_x_list.sort()


import time

start = time.time()
print(solution([1, 4, 0]))
end = time.time()
print end - start
