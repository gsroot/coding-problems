def solution(A):
    ret = 0
    min_avg = float(A[0] + A[1]) / 2
    for i in xrange(len(A) - 1):
        avg = float(sum(A[i:i + 2])) / 2
        if avg < min_avg:
            min_avg = avg
            ret = i
        if i < len(A) - 2:
            avg = float(sum(A[i:i + 3])) / 3
        if avg < min_avg:
            min_avg = avg
            ret = i
    return ret


print(solution([5, 5, 1, 1, 1]))
