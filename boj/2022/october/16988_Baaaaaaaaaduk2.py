# 돌 2개를 두어 죽일 수 있는 상대 돌의 최대 갯수 구하기

# n, m
# 0 빈 칸, 1 나의 돌, 2 상대 돌

# 1. 돌 2개 두어 나올 수 있는 모든 경우 구하기
# 2. 각각의 경우마다 bfs를 통해 상대돌이 몇 개 죽는지 체크
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

check_list = [] # 빈 칸 위치
opponent = [] # 상대 돌 위치

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check_list.append((i, j))
        elif graph[i][j] == 2:
            opponent.append((i, j))
# print(check_list)

two_pick_list = list(combinations(check_list, 2))
# print(two_pick_list)

def bfs(a, b):

    q = deque()
    q.append((a, b))
    visited[a][b] = True

    global total
    count = 1
    tmp = 0

    while q:

        node = q.popleft()
        x, y = node[0], node[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 2:
                        q.append((nx, ny))
                        count += 1
                        visited[nx][ny] = True

                    elif graph[nx][ny] == 0:
                        tmp = -1
                        count = 0

    if tmp == 0:
        total += count

answer = []
for i in two_pick_list:

    x1, y1 = i[0][0], i[0][1]
    x2, y2 = i[1][0], i[1][1]

    graph[x1][y1] = 1
    graph[x2][y2] = 1

    total = 0

    visited = [[False for _ in range(m)] for _ in range(n)]

    for j in opponent:
        a, b = j[0], j[1]
        if not visited[a][b]:
            bfs(a, b)

    answer.append(total)

    graph[x1][y1] = 0
    graph[x2][y2] = 0

print(max(answer))