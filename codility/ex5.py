def solution(A):
    N = len(A)
    nums = N * [0]
    for i in range(N):
        if A[i] - 1 < len(nums) and nums[A[i] - 1] == 0:
            nums[A[i] - 1] = A[i]

    for i in range(len(nums)):
        if nums[i] == 0:
            return 0
    return 1
