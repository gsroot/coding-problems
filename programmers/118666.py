def solution(survey, choices):
    # 선택지를 점수로 매핑하는 딕셔너리
    choice_to_score = {1: -3, 2: -2, 3: -1, 4: 0, 5: 1, 6: 2, 7: 3}
    # 각 성격 유형의 초기 점수 설정
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    # survey와 choices 배열을 순회하며 점수 계산
    for i, survey_type in enumerate(survey):
        choice_score = choice_to_score[choices[i]]
        if choice_score < 0:  # 선택지가 비동의를 나타내는 경우
            scores[survey_type[0]] += abs(choice_score)
        else:  # 선택지가 동의를 나타내는 경우
            scores[survey_type[1]] += choice_score

    # 각 지표별 최종 성격 유형 결정
    personality_type = ''
    for indicator in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if scores[indicator[0]] >= scores[indicator[1]]:
            personality_type += indicator[0]
        else:
            personality_type += indicator[1]

    return personality_type


# 함수 호출 테스트
test_cases = [
    (["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]),
    (["TR", "RT", "TR"], [7, 1, 3]),
]

result = [solution(*test_case) for test_case in test_cases]
print(result)
