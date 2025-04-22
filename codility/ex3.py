def solution(A):
    nums = [i for i in range(1, len(A) + 2)]
    for i in range(len(A)):
        nums[A[i] - 1] = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            return nums[i]
