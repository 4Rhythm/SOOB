# N x N, 1 x 1 땅, 각각의 땅에는 나라가 하나씩 존재
# r, c 나라 => A[r][c]명
#
# 인접한 나라 사이엔 국경선
#
# 인구 이동
#     1. 국경선 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하 => 국경선 open
#     2. 가능한 국경선 다 열리면 인구 이동 시작
#     3. 인접한 칸 통해 이동 가능하면 => 연합
#     4. 연합의 각 칸의 값은 = 연합의 인구수 / 연합 이루고 있는 칸의 개수
#     5. 연합 해체, 국경선 닫음



# 풀이 참고
from collections import deque

n, l, r = map(int, input().split())
graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
# print(graph)
# print(visited)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    tmp = []

    q.append((x, y))
    tmp.append((x, y))
    visited[x][y] = True

    while q:
        # node = q.popleft()
        # x, y = node[0], node[1]
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    tmp.append((nx, ny))
    return tmp

answer = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i, j)

                if len(union) > 1:
                    flag = 1

                    num = 0

                    for x, y in union:
                        num += graph[x][y]
                    num = num // len(union)

                    # num = sum([graph[x][y] for x, y in union]) // len(union)

                    for x, y in union:
                        graph[x][y] = num
    if flag == 0:
        break
    answer += 1

print(answer)