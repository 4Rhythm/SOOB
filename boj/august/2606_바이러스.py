def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            # print("not visited! %d" %i)
            dfs(graph, i, visited)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
answer = 0

for i in visited:
    if i == True:
        answer += 1

print(answer - 1) # 1번 컴퓨터 제외