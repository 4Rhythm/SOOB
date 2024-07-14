# 1번부터 N번까지 번호가 매겨져 있는 도시들
# 도시들 사이에는 길 (길이 없을 수도 있음)

# 어느 한 도시에서 출발, N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로
# 한 번 갔던 도시로는 다시 갈 수 없음 (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)

# 가장 적은 비용을 들이는 여행 계획

# 각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태
# W[i][j] => 도시 i에서 도시 j로 가기 위한 비용

# 비용은 대칭적이지 않음 (W[i][j] != W[j][i])
# 모든 도시간의 비용은 양의 정수
# W[i][i] = 0

# 도시 i에서 도시 j로 갈 수 없는 경우도 있음 (W[i][j] = 0)

# N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로 구하기

# 첫째 줄: 도시의 수 N (2 ≤ N ≤ 10)
# 다음 N개의 줄: 비용 행렬, 각 행렬의 성분은 1,000,000 이하의 양의 정수, 갈 수 없는 경우는 0
# 항상 순회할 수 있는 경우만 입력으로 주어짐

n = int(input())

global min_path
min_path = 20000000

path = []

def dfs(now, total, visited):
    if all(visited):
        global min_path

        if path[now][i] != 0:
            total += path[now][i]
            min_path = min(min_path, total)
            return

    for j in range(n):
        if not visited[j]:
            if path[now][j] != 0:
                visited[j] = True
                dfs(j, total + path[now][j], visited)
                visited[j] = False


for _ in range(n):
    path.append(list(map(int, input().split())))


for i in range(n):
    total = 0
    visited = [False for _ in range(n)]
    visited[i] = True

    dfs(i, total, visited)

print(min_path)