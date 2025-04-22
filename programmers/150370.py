from datetime import datetime, timedelta


def add_months_to_date(date, months):
    """
    지정된 날짜에 특정 개월 수를 더하는 함수입니다. 이 함수는 모든 달을 28일로 간주합니다.
    이 함수는 다양한 달의 길이와 윤년을 고려하지 않습니다.
    """
    new_year = date.year + (date.month + months - 1) // 12
    new_month = (date.month + months - 1) % 12 + 1
    new_day = date.day

    return datetime(new_year, new_month, new_day)


def solution(today, terms, privacies):
    # 각 약관의 유효 기간을 파싱하여 저장합니다.
    term_duration = {term.split()[0]: int(term.split()[1]) for term in terms}

    # today를 datetime 객체로 변환합니다.
    today_date = datetime.strptime(today, "%Y.%m.%d")

    # 파기해야 할 개인정보를 추적하기 위한 리스트입니다.
    expired_privacies = []

    for i, privacy in enumerate(privacies, start=1):
        collection_date_str, term_key = privacy.split()
        collection_date = datetime.strptime(collection_date_str, "%Y.%m.%d")

        # 수집 일자에 해당 약관의 유효기간을 더하여 만료 날짜를 계산합니다.
        expiration_date = add_months_to_date(collection_date, term_duration[term_key])

        # 만료 날짜와 오늘 날짜를 비교하여 파기 여부를 결정합니다.
        if today_date >= expiration_date:
            expired_privacies.append(i)

    return expired_privacies


# 함수 호출 테스트
test_cases = [
    ("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]),
    ("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]),
]
result = [solution(*test_case) for test_case in test_cases]
print(result)
