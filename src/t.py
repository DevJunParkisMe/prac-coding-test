def per(lst):
    ## 선행 종료 조건
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    
    ## 실제 계산 코드
    l = []
    
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[:i] + lst[i+1:]

        ## 재귀문
        for p in per(rem_lst):
            l.append([m]+p)
    #
    #
    return l