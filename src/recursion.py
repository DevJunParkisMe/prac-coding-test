# 누적계산 재귀, 주니어개발자 해결법 Memozation: buffer, cache 만듬(딕셔너리 사용)
__fibo_cache_ = {}

def fibonacci(n):
    if n in __fibo_cache_:
        return __fibo_cache_[n]
    else:
        __fibo_cache_[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
        return __fibo_cache_[n]

# 꼬리재귀, 컴파일러에서 강제로 for loop로 치환하여 계산
def maximum(lst, acc=0):
    if lst == []:
        return acc
    else:
        return maximum(lst[1:], acc if acc > lst[0] else lst[0])

if __name__ == "__main__":
    # print(fibonacci(5000)) # RecursionError, 파이썬 재귀함수는 1000번까지만 순회
    print(maximum([1,2,3,5,2]))
