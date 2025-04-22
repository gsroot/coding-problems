def make_last_char_index(S, last_list, c, i):
    if S[i] == c:
        last_list[i] = i
    elif i > 0:
        last_list[i] = last_list[i - 1]


def solution(S, P, Q):
    ret = []
    last_A, last_C, last_G, last_T = [-1] * len(S), [-1] * len(S), [-1] * len(S), [-1] * len(S)
    for i in xrange(len(S)):
        make_last_char_index(S, last_A, 'A', i)
        make_last_char_index(S, last_C, 'C', i)
        make_last_char_index(S, last_G, 'G', i)
        make_last_char_index(S, last_T, 'T', i)
    for i in xrange(len(P)):
        if last_A[Q[i]] >= P[i]:
            ret.append(1)
        elif last_C[Q[i]] >= P[i]:
            ret.append(2)
        elif last_G[Q[i]] >= P[i]:
            ret.append(3)
        elif last_T[Q[i]] >= P[i]:
            ret.append(4)

    return ret


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
