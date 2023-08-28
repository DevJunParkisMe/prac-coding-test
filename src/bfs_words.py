from collections import deque

def word_conversion(begin, target, words):
    # 초기값
    result = 0
    queue = deque()
    queue.append([begin,0])
    visited = [0] * len(words)
    # 계산
    while queue:
        word, result = queue.popleft()
        if word == target: 
            return result
        for i in range(len(words)):
            if not visited[i]:
               if sum(x != y for x,y in zip(word, words[i])) == 1:
                    queue.append([words[i], result+1])
                    visited[i] = 1
    return 0
    # 결과값
    pass