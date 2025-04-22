# https://leetcode.com/problems/strong-password-checker/
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        # 1) 문자 종류 부족 개수 계산
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_type = 3 - (has_lower + has_upper + has_digit)

        # 2) 연속 반복 구간 길이 수집
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 3
                # 가능한 만큼 늘려가며 길이 계산
                while i + 1 < n and password[i + 1] == password[i]:
                    length += 1
                    i += 1
                repeats.append(length)
            i += 1

        # 연속 구간당 필요한 교체 횟수
        replacements = sum(k // 3 for k in repeats)

        # 3) 길이에 따라 분기
        if n < 6:
            # 삽입을 통해 길이를 6으로 채우면서 부족한 문자 종류도 해결
            return max(missing_type, 6 - n)

        elif n <= 20:
            # 길이는 적정 범위, 교체 혹은 문자 종류 해결
            return max(missing_type, replacements)

        else:
            # n > 20: 반드시 삭제 필요
            over_len = n - 20
            to_delete = over_len

            # 최적 삭제를 위해 (mod, 길이) 쌍으로 정렬
            buckets = [(k % 3, k) for k in repeats]
            buckets.sort()

            # 1) mod==0 구간부터, 1개 삭제로 교체 1회 절약
            for mod, k in buckets:
                if to_delete <= 0:
                    break
                if mod == 0:
                    # 1개 삭제 시 교체 1회 감소
                    to_delete -= 1
                    replacements -= 1

            # 2) mod==1 구간에 2개 삭제로 교체 1회 절약
            for mod, k in buckets:
                if to_delete <= 0:
                    break
                if mod == 1 and k >= 4:
                    delete_cnt = min(to_delete, 2)
                    to_delete -= delete_cnt
                    if delete_cnt == 2:
                        replacements -= 1

            # 3) 나머지 구간: 3개 삭제로 교체 1회 절약
            # 남은 삭제량으로 가능한 만큼
            if to_delete > 0:
                # 3개 삭제마다 replacements 1회 줄어듦
                replacements -= to_delete // 3

            # 총 삭제 + (남은 교체 vs 부족 타입)
            return over_len + max(missing_type, replacements)


if __name__ == "__main__":
    sol = Solution()
    tests = ["a", "aA1", "1337C0d3"]
    for pw in tests:
        result = sol.strongPasswordChecker(pw)
        print(f'Input: password = "{pw}"')
        print(f"Output: {result}\n")
