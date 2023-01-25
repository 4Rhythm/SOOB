# 익은 토마토들의 인접한 곳에 있는 익기 않은 토마토들은 익게 됨
# 대각선은 X, 상하좌우만
# 며칠 지나야 다 익게 되는지, 최소 일수 구하기
from collections import deque

dz = [0, 0, 0, 0, 1, -1]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]

def bfs(queue):
    while queue:
        node = queue.popleft()
        z, x, y = node[0], node[1], node[2]

        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz, nx, ny))

m, n, h = map(int, input().split())
box = []
for i in range(h):
    tmp_box = []
    for j in range(n):
        tmp = list(map(int, input().split()))
        tmp_box.append(tmp)
    box.append(tmp_box)

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))
bfs(queue)

answer = 0
for i in box:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
        answer = max(max(j), answer)
print(answer - 1)
