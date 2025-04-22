def solution(A):
    if len(A) == 0:
        return 0
    cnt = 1
    A.sort()
    seen = A[0]
    for i in xrange(1, len(A)):
        if A[i] != seen:
            seen = A[i]
            cnt += 1
    return cnt


import time

import factory

start = time.time()
print(solution(factory.get('random').get_list(size=100000, min=-1000000, max=1000000)))
end = time.time()
print end - start
