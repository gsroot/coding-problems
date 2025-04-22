def find(phone_book):
    found = False
    all_matches = [[] for _ in range(10)]
    for x in phone_book:
        all_matches[int(x[0])].append(x)
    for i in range(10):
        matches = all_matches[i]
        cnt = len(matches)
        if cnt < 2:
            continue
        if [x for x in matches if len(x) == 1]:
            return True
        found |= find([x[1:] for x in matches])
        if found:
            return True
    return False


def solution(phone_book):
    return not find(phone_book)


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))
    print(solution(["1232", "2232", "123", "45", "99"]))
