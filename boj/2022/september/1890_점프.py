# N x N 점수판
# 가장 왼쪽 위 -> 가장 오른쪽 아래
# 각 칸에 적혀있는 수 = 현재 칸에서 갈 수 있는 거리
# 오른쪽이나 아래로만 이동 가능

# bfs? dfs? 파생되는 루트를 다 체크하면 되지 않나?
from collections import deque

answer = 0
graph = []

#    우, 하
dx = [1, 0]
dy = [0, 1]

n = int(input())

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# print(graph)

start_x, start_y = 0, 0

def dfs(x, y):
    global answer

    num = graph[x][y]

    if num == 0:
        answer += 1
        return

    count = 0

    for i in range(2):
        count += 1

        nx = x + (dx[i] * num)
        ny = y + (dy[i] * num)

        if nx < n and ny < n:
            dfs(nx, ny)

def bfs(x, y):
    global answer

    check = deque()
    check.append([x, y])

    while check:

        tmp = check.popleft()

        x = tmp[0]
        y = tmp[1]

        num = graph[x][y]

        if num == 0:
            answer += 1

        else:
            for i in range(2):
                nx = x + (dx[i] * num)
                ny = y + (dy[i] * num)

                if nx < n and ny < n:
                    check.append([nx, ny])

# dfs(start_x, start_y)
# print(answer)
bfs(start_x, start_y)
print(answer)