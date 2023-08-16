def coin_split(total_value=0):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count = count + (total_value // coin)
        total_value = total_value % coin

    return count

def law_of_large_numbers(p1, p2):
    _, m, k = p1

    p2.sort() # list 오름차순
    first = p2[-1]
    second = p2[-2]
    result = 0

    # 계산
    while True:
        for i in range(k):
            if m == 0:
                break  
            result = result + first
            m = m - 1
        if m == 0:
            break
        result = result + second
        m = m - 1

    return result

def count_with_three_in_time(h):
    # 초기값
    count = 0
    # 계산
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count = count + 1
    # 반환값
    return count

def k_knight(p):
    ## ord('a') = 97 (ASCII 코드 변환)
    ## 현재 나이트의 위치
    column = ord(p[0]) - ord('a') + 1 # 0이 아니라 1부터 시작
    row = int(p[1])

    # 나이트가 이동할 수 있는 8가지 방향
    steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
    
    # 이동 가능 여부 확인
    ## 체스판이 중요한게 아님 !! 
    ### 나이트의 이동 가능 여부가 중요함 !!!
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result = result + 1
    
    return result

def find_prime(numbers):
    from itertools import permutations
    # 초기값
    count = 0
    list_numbers = list(numbers) # 문자열로 들어온 숫자를 뜯어서 list로 반환
    num = []
    # 계산
    ## 순열/조합
    for i in range(1, len(list_numbers)+1):
        num.append(permutations(list_numbers, i))
    # 반환
    return count
if __name__ == "__main__":
    pass