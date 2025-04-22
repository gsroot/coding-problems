# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 특수 경우: 행 수가 1이거나 문자열 길이 이하일 때 변환 불필요
        if numRows == 1 or numRows >= len(s):
            return s

        # 각 행에 해당하는 문자열을 저장할 리스트 초기화
        rows = [""] * numRows
        current_row = 0  # 현재 추가 중인 행 인덱스
        going_down = False  # 방향 플래그: False면 위로, True면 아래로

        # 문자열의 각 문자에 대해
        for char in s:
            rows[current_row] += char

            # 첫 행 또는 마지막 행에 도달하면 방향 전환
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # 방향에 따라 다음 행으로 이동
            current_row += 1 if going_down else -1

        # 모든 행을 순서대로 합쳐서 반환
        return "".join(rows)


if __name__ == "__main__":
    examples = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ]
    for s, numRows, expected in examples:
        result = Solution().convert(s, numRows)
        print(
            f"convert({s!r}, {numRows}) = {result!r}"
            f"  {'✓' if result == expected else '✗ (expected ' + expected + ')'}"
        )
