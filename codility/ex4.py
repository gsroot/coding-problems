def solution(X, A):
    positions = X * [0]
    leaf_cnt = 0
    for i in range(len(A)):
        if positions[A[i] - 1] == 0:
            positions[A[i] - 1] = A[i]
            leaf_cnt += 1
            if leaf_cnt == X:
                return i
    return -1
