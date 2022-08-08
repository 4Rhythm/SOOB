# 무지성 dfs로 접근했는데 안되더라..
# 최단거리 문제 => bfs로 푸는 걸로..

# n x m 크기의 배열
# 1은 이동할 수 있는 칸, 0은 이동 X
# (1, 1) -> (n, m) 최소의 칸 수

# 칸 셀 때엔 시작, 도착 위치 모두 포함
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
answer = []
x, y = 0, 0 # 시작 지점

# count = 0 # 이동한 칸 수

queue = deque()

# def dfs(graph, x, y, count):
#
#     count += 1
#     graph[x][y] = 0
#
#     # 그래프 출력 (확인용)
#     print(count)
#     for i in graph:
#         print(i)
#
#     print()
#
#     for j in range(4):
#         nx = x + dx[j]
#         ny = y + dy[j]
#
#         if 0 <= nx < n and 0 <= ny < m:
#             if nx == n - 1 and ny == m - 1:
#                 count += 1
#                 graph[nx][ny] = 0
#                 answer.append(count)
#                 break
#
#             if graph[nx][ny] == 1:
#                 dfs(graph, nx, ny, count)

def bfs(graph, x, y):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    return graph[n - 1][m - 1]

n, m = map(int, input().split())

# 그래프 입력받기
for i in range(n):
    data = str(input())
    tmp = []
    for j in range(m):
        tmp.append(int(data[j:j+1]))
    graph.append(tmp)

# # 그래프 출력 (확인용)
# print("*****graph*****")
# for i in graph:
#     print(i)
# print("**********")

# print(min(answer))

print(bfs(graph, x, y))