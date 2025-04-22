def solution(X, Y, D):
    jump_cnt = (Y - X) / D
    if (Y - X) % D != 0:
        jump_cnt += 1
    return jump_cnt
