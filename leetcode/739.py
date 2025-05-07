# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # 인덱스를 저장할 스택

        for i, cur_temp in enumerate(temperatures):
            # 스택이 비어 있지 않고,
            # 현재 온도가 스택[top]에 해당하는 날의 온도보다 높으면
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                answer[prev_i] = i - prev_i
            # 아직 더 따뜻한 날을 못 만난 오늘을 스택에 push
            stack.append(i)

        # 스택에 남은 인덱스들은 더 따뜻한 날이 없는 경우이므로 answer에 0이 이미 설정돼 있음
        return answer


if __name__ == "__main__":
    result = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(result)
