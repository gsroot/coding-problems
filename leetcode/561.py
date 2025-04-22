# https://leetcode.com/problems/array-partition/
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    result = Solution().arrayPairSum(nums)
    print(result)
