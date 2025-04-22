# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)
