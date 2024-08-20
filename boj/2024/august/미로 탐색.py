# N×M크기의 배열로 표현되는 미로
# 1은 이동할 수 있는 칸
# 0은 이동할 수 없는 칸
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하기
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있음
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함

from collections import deque

N, M = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    tmp = str(input())
    tmp_list = list(map(int, tmp))
    graph.append(tmp_list)

queue = deque([[0, 0, 1]])

while queue:
    node = queue.popleft()
    nowX, nowY, nowCnt = node[0], node[1], node[2]

    for i in range(4):
        nx = nowX + dx[i]
        ny = nowY + dy[i]

        if nx == N - 1 and ny == M - 1:
            print(nowCnt + 1)
            exit()

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            queue.append([nx, ny, nowCnt + 1])
            graph[nx][ny] = 0

