# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 현재 높이와 너비
            h = min(height[left], height[right])
            w = right - left
            # 면적 계산 및 최댓값 갱신
            max_area = max(max_area, h * w)

            # 더 낮은 쪽을 안쪽으로 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area




if __name__ == '__main__':
    tests = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]
    for test in tests:
        result = Solution().maxArea(test)
        print(result)