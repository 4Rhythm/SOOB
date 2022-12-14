# n x m 연구소
#
# 빈 칸(0), 벽(1), 바이러스(2)
#
# 세울 수 있는 벽의 수는 3개(3개 다 세워야 함)
#
# 안전 영역의 최댓값 구하기
import copy
import itertools
from collections import deque

n, m = map(int, input().split())
graph = []
virus = []
possible = []
answer = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            possible.append((i, j))

data = list(itertools.combinations(possible, 3))
# print(data)
# print(len(data))

def bfs(x, y, test_graph):
    queue = deque()
    queue.append((x, y))

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if test_graph[nx][ny] == 0:
                    test_graph[nx][ny] = 2
                    queue.append((nx, ny))
                else:
                    continue

for i in data:
    test_graph = copy.deepcopy(graph)
    one_x, one_y = i[0][0], i[0][1]
    two_x, two_y = i[1][0], i[1][1]
    three_x, three_y = i[2][0], i[2][1]

    test_graph[one_x][one_y] = 1
    test_graph[two_x][two_y] = 1
    test_graph[three_x][three_y] = 1

    for j in virus:
        bfs(j[0], j[1], test_graph)

    count = 0
    for k in test_graph:
        for l in k:
            if l == 0:
                count += 1

    answer.append(count)

print(max(answer))