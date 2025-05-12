# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 값 → 인덱스 매핑
        idx_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            # complement가 이미 map에 있으면 정답 발견
            if complement in idx_map:
                return [idx_map[complement], i]
            # 현재 값 저장 (나중에 다른 숫자의 complement가 될 수 있음)
            idx_map[num] = i

        # 문제 조건상 반드시 하나의 해가 있으므로 여기까지 도달하지 않습니다.
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)
