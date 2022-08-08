# 익지 않은 토마토 => 익은 토마토가 인접한 곳에 있다면 1일 후 익음
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 X

from collections import deque

# BFS 함수 정의
def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1 # (hint) 이렇게 값을 할당해준다면 graph의 최대값이 곧 day가 됨
                    queue.append([nx, ny])

m, n = map(int, input().split())

graph = []
queue = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0

for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# visited = [[0] * m] * n

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1) # 익지 않은 토마토가 있다면 -1
            exit(0)
    day = max(day, max(i))
print(day-1) # 1부터 시작했기에 -1 해줌