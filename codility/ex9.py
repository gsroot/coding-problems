def solution(A):
    cnt = 0
    num_to_add = 0
    for i in xrange(len(A)):
        if A[i] == 0:
            num_to_add += 1
        elif A[i] == 1:
            cnt += num_to_add
            if cnt > 1000000000:
                return -1
    return cnt
