def solution(N, A):
    ret = N * [0]
    saved_max = 0
    cur_max = 0
    for num in A:
        if num <= N:
            pos = num - 1
            if ret[pos] < saved_max:
                ret[pos] = saved_max + 1
            else:
                ret[pos] += 1
            if ret[pos] > cur_max:
                cur_max = ret[pos]
        else:
            saved_max = cur_max
    for i in xrange(N):
        if ret[i] < saved_max:
            ret[i] = saved_max
    return ret
