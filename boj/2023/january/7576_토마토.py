# 익은 토마토들의 인접한 곳에 있는 익기 않은 토마토들은 익게 됨
# 대각선은 X, 상하좌우만
# 며칠 지나야 다 익게 되는지, 최소 일수 구하기
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(queue):
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    queue.append((nx, ny))

m, n = map(int, input().split())
box = []
for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
bfs(queue)

answer = 0
for i in box:
    if 0 in i:
        print(-1)
        exit()
    answer = max(max(i), answer)
print(answer - 1)
