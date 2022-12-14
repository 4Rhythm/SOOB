# 각 지점의 높이가 주어짐

# 비 = 4 => 4 이하의 모든 지점 물에 잠김
# 물에 잠기면서 잠기지 않은 안전한 영역(고립되는 지점)들이 생기고 그 개수가 나올거임
# 그 개수의 최댓값을 구하고 싶음
import sys
sys.setrecursionlimit(10**7)

n = int(input())

graph = []
answer = []

min_rain, max_rain = 1, 1

for i in range(n):
    data = list(map(int, input().split()))
    max_rain = max(max_rain, max(data))
    min_rain = min(min_rain, min(data))
    graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물에 잠긴 영역 표시된 그래프
def setting(h):
    global safe

    safe = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:
                safe[i][j] = graph[i][j]

def dfs(x, y):
    safe[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if safe[nx][ny] != 0:
                dfs(nx, ny)

# 높이의 최솟값부터 최댓값까지 각각 dfs 실행
for i in range(min_rain, max_rain):
    setting(i)
    count = 0
    for j in range(n):
        for k in range(n):
            if safe[j][k] != 0:
                dfs(j, k)
                count += 1
    answer.append(count)

# 아무 지역도 물에 잠기지 않을 수도 있음
if len(answer) == 0:
    print(1)
else:
    print(max(answer))