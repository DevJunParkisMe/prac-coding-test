n = 0
m = 0
graph = []
  
def dfs(x,y):
    # 선행 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

def ice(mat):
    # 1. 초기화
    global n
    n = len(mat)
    global m
    m = len(mat[0])
    global graph
    graph = mat
    result = 0
    # 2. 계산
    # 2-1. 연결되어 있는지 확인해야 됨
    # 2-2. 연결되어 있으면 count를 1!!
    # Q. 연결 여부는 어떻게 알고 있나?
    ## -- x,y 이용
    ## def find_con(x,y):
    ##      if len(m) and len(m[0])
            ## x는 len(m)이랑 비교하나요?
            ## len(m[0])이랑 비교하나요?
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
               result = result+1
    # 3. 반환
            
    return result

