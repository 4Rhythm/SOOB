# 1은 집이 있는 곳, 0은 집이 없는 곳

# 연결되어 있는 집들을 하나의 단지라고 함
# 총 몇 단지가 있는지, 각 단지내 집 수는 몇인지 구하기

def dfs(x, y):

    graph[x][y] = 0 # 집 확인
    block[x][y] = num # 단지 부여

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if block[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)

graph = [] # 지도
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 0 # 총 단지수

n = int(input())
for i in range(n):
    value = input()
    tmp = list(map(int, value))
    graph.append(tmp)

# <그림 2> 와 같이 단지수가 체크된 지도
block = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and block[i][j] == 0: # graph 값이 1이고(집이 있고), 방문을 안한 곳이라면 dfs 호출
            num += 1
            dfs(i, j)

# 각 단지내 집의 수 count
for i in range(1, num + 1):
    tmp = 0
    for j in block:
        tmp += j.count(i)
    answer.append(tmp)

answer.sort()

print(num)
for i in answer:
    print(i)