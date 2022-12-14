# 상근이는 자신의 친구와 친구의 친구를 초대하기로 함
# 동기 N명, 학번은 1부터 N // 상근 학번 1
from collections import deque

depth, count = 0, 0

def bfs(visited):
    queue = deque()

    visited[1] = 1
    queue.append(1)

    global depth
    global count
    total_pop_count = len(graph[1]) + 1 # 친구의 친구까지이므로, 친구(1) + 친구의 친구(len(graph[1]))
    pop_count = 0

    while queue:
        node = queue.popleft()
        pop_count += 1

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                queue.append(i)
        if pop_count == total_pop_count:
            break

    print(count)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(visited)