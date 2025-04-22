def solution(A):
    sum_part1 = 0
    sum_part2 = sum(A)
    min_diff = None
    for P in range(1, len(A)):
        sum_part1 += A[P - 1]
        sum_part2 -= A[P - 1]
        diff = abs(sum_part1 - sum_part2)
        if min_diff == None or diff < min_diff:
            min_diff = diff
    return min_diff
