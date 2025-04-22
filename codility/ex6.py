def solution(A):
    N = len(A)
    positives = N * [0]
    for n in A:
        if n > 0:
            if n <= N:
                positives[n - 1] = n
    for i in xrange(len(positives)):
        if positives[i] == 0:
            return i + 1
    return N + 1
