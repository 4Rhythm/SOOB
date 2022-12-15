from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
parents = list(map(int, input().split()))
# print(parents)

for i in range(0, n):
    if parents[i] == -1:
        continue
    graph[parents[i]].append(i)
# print(graph)

dNode = int(input())

for i in graph:
    if dNode in i:
        i.remove(dNode)

queue = deque()
queue.append(dNode)

while len(queue) > 0:
    node = queue.popleft()

    for i in graph[node]:
        queue.append(i)

    graph[node] = [999]
# print(graph)

leaf = 0
for i in graph:
    if len(i) == 0:
        leaf += 1
print(leaf)