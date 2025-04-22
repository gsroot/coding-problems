from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == current:
                nums.pop(i)
            else:
                current = n
                i += 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))
    print(nums)
