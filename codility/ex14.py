def solution(A):
    A.sort()
    for i in xrange(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0


import time

import factory

start = time.time()
print(solution(factory.get('random').get_list(size=100000, min=-1000000000, max=1000000000)))
end = time.time()
print end - start
