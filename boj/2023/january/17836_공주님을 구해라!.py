# (N, M) 크기의 성 입구 (1, 1)
# 마법의 벽을 피해 (N, M) 위치에 있는 공주님을 구출해야 함
#
# T시간 이내 만나지 못하면 실패
# 한 칸 이동 = 한 시간
#
# 검에 도달하면 벽 무시 가능
#
# 1. 명검에 도달 + 명검부터 n, m 거리
# 2. 벽 피해서 공주까지 거리
# 중 최솟값 구하기?
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, t = map(int, input().split())
graph = []
answer = []

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

visited = [[0] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1 # 1시간부터 시작

while queue:
    tmp = 0

    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if nx == n - 1 and ny == m - 1:
                answer.append(visited[x][y])
                tmp = 1
                break
            elif graph[nx][ny] == 2:
                d = visited[x][y] + (n - 1 - nx) + (m - 1 - ny)
                answer.append(d)
                visited[nx][ny] = visited[x][y] + 1
            elif graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    if tmp == 1:
        break

if len(answer) == 0 or t < min(answer):
    print("Fail")
else:
    print(min(answer))