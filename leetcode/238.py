# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = []
        p = 1
        for n in nums:
            out.append(p)
            p *= n
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
        return out


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = Solution().productExceptSelf(nums)
    print(result)
