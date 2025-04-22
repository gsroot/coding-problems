# https://leetcode.com/problems/reorder-data-in-log-files
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        text_logs = []
        digit_logs = []
        for log in logs:
            parts = log.split(" ", 1)
            id, content = parts[0], parts[1]

            if content[0].isdigit():
                digit_logs.append(log)
            else:
                text_logs.append((content, id))
        text_logs.sort(key=lambda x: (x[0], x[1]))
        return [f"{id} {content}" for content, id in text_logs] + digit_logs


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result = Solution().reorderLogFiles(logs)
    print(result)