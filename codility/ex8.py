def solution(A, B, K):
    cnt = 0
    start = A
    if A % K != 0:
        start += K - (A % K)
        if start > B:
            return cnt
    cnt = (B - start) / K + 1
    return cnt
