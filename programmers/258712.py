def solution(friends, gifts):
    # 각 친구별로 선물을 준 횟수와 받은 횟수를 기록하기 위한 딕셔너리 초기화
    gift_records = {friend: {'given': 0, 'received': 0} for friend in friends}
    # 각 친구별로 다른 친구에게 준 선물의 횟수를 기록하기 위한 딕셔너리 초기화
    gift_exchange = {friend: {other: 0 for other in friends if other != friend} for friend in friends}

    # gifts 리스트를 순회하며 선물을 준 횟수와 받은 횟수, 선물 교환 기록을 업데이트
    for gift in gifts:
        giver, receiver = gift.split()
        gift_records[giver]['given'] += 1
        gift_records[receiver]['received'] += 1
        gift_exchange[giver][receiver] += 1

    # 다음 달에 각 친구가 받게 될 선물의 수를 기록할 딕셔너리 초기화
    next_month_gifts = {friend: 0 for friend in friends}

    # 각 친구별로 선물 교환 기록을 바탕으로 다음 달에 받게 될 선물의 수 계산
    for giver in friends:
        for receiver in friends:
            if giver != receiver:
                # giver가 receiver에게 선물을 더 많이 준 경우, giver가 선물을 받음
                if gift_exchange[giver][receiver] > gift_exchange[receiver][giver]:
                    next_month_gifts[giver] += 1
                # 선물을 준 횟수가 같은 경우, 선물 지수(준 선물 - 받은 선물)가 높은 친구가 선물을 받음
                elif gift_exchange[giver][receiver] == gift_exchange[receiver][giver]:
                    gift_index_giver = gift_records[giver]['given'] - gift_records[giver]['received']
                    gift_index_receiver = gift_records[receiver]['given'] - gift_records[receiver]['received']
                    if gift_index_giver > gift_index_receiver:
                        next_month_gifts[giver] += 1

    # 다음 달에 가장 많은 선물을 받게 될 친구가 받을 선물의 최대 수를 계산하여 반환
    max_gifts_received = max(next_month_gifts.values())
    return max_gifts_received if max_gifts_received > 0 else 0



# 함수 호출 테스트
test_cases = [
    (["muzi", "ryan", "frodo", "neo"],
     ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]),
    (["joy", "brad", "alessandro", "conan", "david"],
     ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
    (["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]),
]

result = [solution(*test_case) for test_case in test_cases]
print(result)
